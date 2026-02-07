from sqlalchemy import String, Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)

    def __repr__(self) -> str:
        return f"<User {self.name}>"