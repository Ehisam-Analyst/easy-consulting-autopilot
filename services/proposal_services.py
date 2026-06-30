from proposal import generate_proposal
from datetime import datetime

def create_proposal(lead):

    filename = generate_proposal(lead)

    return filename

def create_proposal(lead):

    check_existing_customer()

    filename = generate_proposal(lead)

    return filename

def create_proposal(lead):

    print(
        f"[{datetime.now()}] Creating proposal for {lead['company']}"
    )

    filename = generate_proposal(lead)

    print(
        f"[{datetime.now()}] Proposal created."
    )

    return filename

def create_proposal(lead):

    try:

        filename = generate_proposal(lead)

        return filename

    except Exception as e:

        print(e)

        raise