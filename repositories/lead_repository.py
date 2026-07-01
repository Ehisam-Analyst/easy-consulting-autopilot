from sqlalchemy.orm import Session

from project.db_models import Lead


def create_lead(db: Session, lead_data: dict):

    new_lead = Lead(
        company=lead_data["company"],
        industry=lead_data["industry"],
        country=lead_data["country"],
        service=lead_data["service"]
    )

    db.add(new_lead)
    db.commit()
    db.refresh(new_lead)
    return new_lead