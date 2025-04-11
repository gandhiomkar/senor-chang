from pydantic import BaseModel, Field
from sqlalchemy import Text, create_engine, Column, Integer, String, Boolean, ForeignKey
from db.base import Base
import shortuuid


class MessageStore(Base):
    __tablename__ = 'message_store'

    id = Column(Integer, primary_key=True)
    session_id = Column(String)
    message = Column(Text)

class User(Base):
    __tablename__ = 'user_data'

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String)
    target_lang = Column(String)
    target_lvl = Column(String)
    native_lang = Column(String)
    know_eng = Column(Boolean)
    session_id = Column(String)


class MessageFeedback(Base):
    __tablename__ = 'message_feedback'
    
    id = Column(Integer, primary_key=True)
    message_id = Column(Integer)  # Link to message_store table
    session_id = Column(String)
    is_correct = Column(Boolean)
    # mistake = Column(String)

