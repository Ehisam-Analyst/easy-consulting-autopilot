from project.database import Base, engine
from project.db_models import Lead, Proposal

print("Creating database...")

Base.metadata.create_all(bind=engine)

print("Database created successfully!")