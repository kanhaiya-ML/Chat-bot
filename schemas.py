from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ConversationCreate(BaseModel):
    title: Optional[str] = "New Chat"

class ConversationResponse(BaseModel):
    id: str
    title: str
    created_at: datetime

class MessageSend(BaseModel):
    conversation_id: str
    message: str
    web_search: bool = False
    deep_research: bool = False

class MessageResponse(BaseModel):
    conversation_id: str
    role: str
    content: str
    created_at: datetime
    