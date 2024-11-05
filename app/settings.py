"""Settings."""

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

from app.utils import get_env_file_path


class ApplicationSettings(BaseSettings):
    """Application settings."""

    version: str = 'dev'
    port: int = 8000


class OpenAISettings(BaseModel):
    """OpenAI settings."""

    api_secret_key: str = ''
    embedding_model: str = ''
    embedding_dimension: int = 1536


class DaprSettings(BaseModel):
    """Dapr settings."""

    base_url: str = ''
    port: str = ''


class MilvusSettings(BaseModel):
    """Milvus db settings."""

    url: str = ''


class Settings(BaseSettings):
    """Application settings."""

    model_config = SettingsConfigDict(
        env_nested_delimiter='__',
        env_file=get_env_file_path(),
    )

    app: ApplicationSettings = ApplicationSettings()
    openai: OpenAISettings = OpenAISettings()
    dapr: DaprSettings = DaprSettings()
    milvus: MilvusSettings = MilvusSettings()
