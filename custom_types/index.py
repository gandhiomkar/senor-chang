# Pydantic
from pydantic import BaseModel, Field


class AI_Response(BaseModel):
    """AI response to  user."""

    reply: str = Field(description="The reply to user message")
    english_translation: str = Field(description="enlish translation of the reply")
    is_correct: bool = Field(description="True if user did not make any mistakes. False if user made any mistake in his response")
    # mistake: str = Field( description="description of user mistake" 