from sqlalchemy import Column,String,Text,DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import uuid


Base = declarative_base()

def generate_uuid():
    return str(uuid.uuid4())

class Conversation(Base):
    __tablename__ = "Conversation"

    id = Column(String,primary_key=True,default=generate_uuid)
    title = Column(String,default="New Chat")
    created_at = Column(DateTime,default=datetime.utcnow
)

class Message(Base):
    __tablename__ = "Messages"

    id = Column(String,primary_key=True,default=generate_uuid)
    conversation_id = Column(String,nullable=False)
    role = Column(String,nullable=False)
    content = Column(Text,nullable=False)
    created_at = Column(DateTime,default=datetime.utcnow
)

