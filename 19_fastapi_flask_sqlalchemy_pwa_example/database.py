from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

DATABASE_URL = "sqlite:///db.sqlite3"
ASYNC_DATABASE_URL = "sqlite+aiosqlite:///db.sqlite3"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

async_engine = create_async_engine(
    ASYNC_DATABASE_URL,
    echo=False,
)
AsyncSessionLocal = async_sessionmaker(async_engine, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

# For Flask usage
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# For FastAPI usage
async def get_async_db():
    async with AsyncSessionLocal() as session:
        yield session

