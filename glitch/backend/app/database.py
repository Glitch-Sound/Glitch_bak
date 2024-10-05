from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "sqlite:///./glitch.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def setup_fts():
    with SessionLocal() as session:
        session.execute(text("""
            CREATE VIRTUAL TABLE IF NOT EXISTS activities_fts USING fts5(
                rid UNINDEXED,
                activity,
                content='activities',
                content_rowid='rid'
            );
        """))

        session.execute(text("""
            CREATE TRIGGER IF NOT EXISTS activities_ai AFTER INSERT ON activities BEGIN
                INSERT INTO activities_fts(rowid, rid, activity)
                VALUES (new.rid, new.rid, new.activity);
            END;
        """))

        session.execute(text("""
            CREATE TRIGGER IF NOT EXISTS activities_au AFTER UPDATE ON activities BEGIN
                UPDATE activities_fts
                SET activity = new.activity
                WHERE rowid = new.rid;
            END;
        """))

        session.execute(text("""
            CREATE TRIGGER IF NOT EXISTS activities_ad AFTER DELETE ON activities BEGIN
                DELETE FROM activities_fts WHERE rowid = old.rid;
            END;
        """))

        session.commit()
