import json
from dataclasses import dataclass

from openai import OpenAI
from dependency_injector.wiring import Provide, inject

from app.container import Container
from app.domain.models.milvus import CollectionItem, CollectionItemText
from app.settings import Settings
from app.adapters.milvus import MilvusUnitOfWork


@dataclass
class Phrase:
    role: str
    message: str


@dataclass
class Dialog:
    category: str
    conversation: list[Phrase]


def parse_conversation(conversation: list[Phrase]):
    user_phrases = []
    support_phrases = []

    def distribute_phrase(speaker: str, phrase: str):
        match speaker.lower():
            case 'user':
                user_phrases.append(phrase)
            case 'support':
                support_phrases.append(phrase)
            case _:
                pass

    last_speaker = None
    messages = []
    for phrase in conversation:
        speaker = phrase.role
        message = phrase.message.strip()

        if message[-1] not in ['.', '!', '?']:
            message += '.'

        if not last_speaker:
            last_speaker = speaker

        if speaker == last_speaker:
            messages.append(message)
            continue

        full_message = ' '.join(messages)
        distribute_phrase(last_speaker, full_message)

        messages = [message]
        last_speaker = speaker

    else:
        full_message = ' '.join(messages)
        distribute_phrase(last_speaker, full_message)

    return user_phrases, support_phrases


@inject
def load_data_to_milwus(
    data,
    uow: MilvusUnitOfWork = Provide[Container.milvus_uow]
):

    with uow:

        if uow.support_chats.is_collection_exists():
            uow.support_chats.drop_collection()

        uow.support_chats.create_collection()
        uow.support_chats.add(entity=data)


if __name__ == '__main__':
    container = Container()
    container.wire(modules=[__name__])
    settings = Settings()

    container.config.from_dict(settings.model_dump())

    data_path = '/home/ya_boiko/www/shakuro/proko/support-bot/data'
    dialogs_filename = 'dialogs-en_100.json'
    dialogs_path = data_path + '/' + dialogs_filename

    openai_client = OpenAI(api_key=settings.openai.api_secret_key)

    with open(dialogs_path, 'r', encoding='utf-8') as f:
        json_data = json.load(f).get('dialogs', [])

        dialogs = []
        for dialog in json_data:
            conversation = [Phrase(role=p['role'], message=p['message']) for p in dialog['conversation']]
            dialogs.append(
                Dialog(
                    category=dialog['category'],
                    conversation=conversation,
                )
            )

    user_phrases = []
    support_phrases = []
    for dialog in dialogs:
        user_phrase, support_phrase = parse_conversation(dialog.conversation)
        user_phrases.extend(user_phrase)
        support_phrases.extend(support_phrase)

    # user_phrases_embeddings = openai_client.embeddings.create(
    #     input=user_phrases[:len(support_phrases)],
    #     model=settings.openai.embedding_model
    # )
    # vectors = [phrase.embedding for phrase in user_phrases_embeddings.data]

    # with open("123456789.json", 'r', encoding='utf-8') as f:
    #     f.write(json.dumps(vectors))

    with open("123456789.json", 'r', encoding='utf-8') as f:
        vectors = json.load(f)

    data = []
    for support_phrase, user_phrase, vector in zip(support_phrases, user_phrases, vectors):
        data.append(
            CollectionItem.create(
                vector=vector,
                text=CollectionItemText(
                    question=user_phrase,
                    answer=support_phrase,
                ),
                subject='history',
            )
        )

    res = load_data_to_milwus(data)
