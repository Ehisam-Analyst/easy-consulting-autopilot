from sqlalchemy.orm import Session

from project.db_models import Proposal


def create_proposal_record(
    db: Session,
    lead_id: int,
    filename: str
):
    proposal = Proposal(
        lead_id=lead_id,
        filename=filename
    )

    db.add(proposal)
    db.commit()
    db.refresh(proposal)

    return proposal