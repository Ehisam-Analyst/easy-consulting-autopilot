from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime, UTC
from project.database import Base


class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    company = Column(String, nullable=False)
    industry = Column(String, nullable=False)
    country = Column(String, nullable=False)
    service = Column(String, nullable=False)

class Proposal(Base):
    __tablename__ = "proposals"

    id = Column(Integer, primary_key=True, index=True)

    lead_id = Column(
        Integer,
        ForeignKey("leads.id"),
        nullable=False
    )

    filename = Column(
        String,
        nullable=False
    )

    generated_at = Column(
        DateTime,
        default=lambda: datetime.now(UTC)
    )