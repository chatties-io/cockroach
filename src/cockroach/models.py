import datetime

from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class RssFeed(Base):
    __tablename__ = "rss_feed"
    id = Column(Integer, primary_key=True)
    url = Column(String(1000), unique=True, nullable=False)
    last_visit = Column(
        DateTime,
        default=datetime.datetime(1970, 1, 1, 0, 0, 0, 0)
    )
    lang = Column(String(3), nullable=False)

    def __repr__(self):
        return f"<RssFeed url=\"{self.feed}\">"


class Article(Base):
    __tablename__ = "article"
    id = Column(Integer, primary_key=True)
    url = Column(String(1000), unique=True, nullable=False)

    def __repr__(self):
        return f"<Article url=\"{self.url}\">"


def ArticleWord(Base):
    __tablename__ = "article_word"
    article = relationship("Article", primary_key=True)
    word = Column(String(255), primary_key=True)
    count = Column(Integer)