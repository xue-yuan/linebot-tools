from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy import Text as TextField
from sqlalchemy.orm import relationship

from database import Base


class Keyword(Base):
    __tablename__ = "keywords"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    parent_id = Column(Integer)

    texts = relationship("Text")
    files = relationship("File")
    images = relationship("Image")


class Text(Base):
    __tablename__ = "texts"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    keyword_id = Column(Integer, ForeignKey("keywords.id"))
    content = Column(TextField, nullable=True)


class File(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    keyword_id = Column(Integer, ForeignKey("keywords.id"))
    content = Column(TextField, nullable=True)


class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    keyword_id = Column(Integer, ForeignKey("keywords.id"))
    content = Column(TextField, nullable=True)
