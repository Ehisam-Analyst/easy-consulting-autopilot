from repositories.lead_repository import create_lead
from project.proposal import generate_proposal


def create_proposal(db, lead_data):
    # Save the lead
    saved_lead = create_lead(db, lead_data)

    # Generate the proposal using your existing code
    filename = generate_proposal(lead_data)

    # Later we will save proposal metadata here

    return {
        "lead": saved_lead,
        "filename": filename
    }

