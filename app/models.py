import uuid

from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy import String, Integer
from sqlalchemy.dialects.postgresql import UUID


Base = declarative_base()

class Book(Base):
    __tablename__ = "books"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    author: Mapped[str] = mapped_column(String(100), nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)