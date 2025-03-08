from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, text
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    # One-to-Many ilişkiler
    boards = relationship('Board', back_populates='owner', cascade="all, delete-orphan")
    comments = relationship('Comment', back_populates='user', cascade="all, delete-orphan")


class Board(Base):
    __tablename__ = 'boards'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    owner_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"))

    owner = relationship('User', back_populates='boards')
    columns = relationship('ColumnsOfBoard', back_populates='board', cascade="all, delete-orphan")


class ColumnsOfBoard(Base):
    __tablename__ = 'columns'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    board_id = Column(Integer, ForeignKey('boards.id', ondelete="CASCADE"))

    board = relationship('Board', back_populates='columns')
    tasks = relationship('Task', back_populates='column', cascade="all, delete-orphan")


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    status = Column(String, default=text("To Do"))
    column_id = Column(Integer, ForeignKey('columns.id', ondelete="CASCADE"))

    column = relationship('ColumnsOfBoard', back_populates='tasks')