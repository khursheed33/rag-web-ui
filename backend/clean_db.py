from sqlalchemy import create_engine, text
from app.core.config import settings

def clean_database():
    engine = create_engine(settings.get_database_url)
    with engine.connect() as conn:
        conn.execute(text("DROP TABLE IF EXISTS processing_tasks CASCADE"))
        conn.execute(text("DROP TABLE IF EXISTS document_uploads CASCADE"))
        conn.execute(text("DROP TABLE IF EXISTS alembic_version CASCADE"))
        conn.execute(text("DROP TABLE IF EXISTS document_chunks CASCADE"))
        conn.execute(text("DROP TABLE IF EXISTS chat_knowledge_bases CASCADE"))
        conn.execute(text("DROP TABLE IF EXISTS documents CASCADE"))
        conn.execute(text("DROP TABLE IF EXISTS knowledge_bases CASCADE"))
        conn.execute(text("DROP TABLE IF EXISTS messages CASCADE"))
        conn.execute(text("DROP TABLE IF EXISTS chats CASCADE"))
        conn.execute(text("DROP TABLE IF EXISTS api_keys CASCADE"))
        conn.execute(text("DROP TABLE IF EXISTS users CASCADE"))
        conn.commit()

if __name__ == "__main__":
    clean_database()
    print("Database cleaned successfully") 