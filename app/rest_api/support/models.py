"""Models."""

from pydantic import BaseModel, Field


class QuestionBase(BaseModel):
    """Question base model."""

    text: str = Field(title="Question text")


class QuestionRequest(QuestionBase):
    """Question model for requests."""


class Answer(BaseModel):
    """Answer model."""

    text: str = Field(title="Answer text")


class AnswerResponse(Answer):
    """Question model for response."""
