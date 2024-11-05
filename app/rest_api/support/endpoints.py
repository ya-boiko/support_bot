"""Endpoints."""

from fastapi import APIRouter

from app.rest_api.api_response import APIResponse

from .models import Answer


router = APIRouter(tags=['Support'], prefix='/api/support')


@router.post('')
async def method() -> APIResponse[Answer]:
    """Generates the answer for the question."""
    pass