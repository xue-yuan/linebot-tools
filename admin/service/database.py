from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from logger import logger


DATABASE_URL = "sqlite:///../../database.db"

engine = create_engine(
    DATABASE_URL,
    echo=True,
    connect_args={
        "check_same_thread": False,  # only need for sqlite
    },
    max_overflow=0,
    pool_recycle=1200,
    pool_size=10,
    pool_timeout=20,
)

Session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


def initialize():
    logger.info("[!] Initialize Database")
    Base.metadata.create_all(bind=engine)


def session(f):
    def wrapper(*args, **kwargs):
        s = Session()
        kwargs["db"] = s
        f(*args, **kwargs)
        s.close()

    return wrapper
