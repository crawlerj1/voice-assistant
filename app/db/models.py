from app.db.base import Base
import uuid
from datetime import datetime
from sqlalchemy import Column, Integer,Text, DateTime, ForeignKey,Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship



class Session(Base):
    __tablename__ = "session"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow, nullable=False)
    closed_at = Column(DateTime(timezone=True), nullable=True)
    status = Column(Text, nullable=False, default="inactive")

    messages = relationship("SessionMessage", back_populates="session", cascade="all, delete-orphan")
    costs = relationship("LLMCostingPerCall", back_populates="session",cascade="all, delete-orphan")

class SessionMessage(Base):
    __tablename__ = "session_message"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    session_id = Column(UUID(as_uuid=True), ForeignKey("session.id", ondelete="CASCADE"), nullable=False)
    role = Column(Text, nullable=False)        # "user" | "assistant"
    content = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow, nullable=False)

    session = relationship("Session", back_populates="messages")
    
class llm_costing_per_call(Base):
    __tablename__ = "llm_costing_per_call"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    session_id = Column(UUID(as_uuid=True), ForeignKey("session.id", ondelete="CASCADE"), nullable=False)
    total_tokens = Column(Integer, nullable=False)
    total_cost = Column(Float, nullable=True)
    ai_model = Column(Text, nullable=False)
    inference_time = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow, nullable=False)

    session = relationship("Session", back_populates="costs")
  