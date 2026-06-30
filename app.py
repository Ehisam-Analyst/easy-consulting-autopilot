from fastapi import FastAPI
from models import Lead
from services.proposal_services import create_proposal
from services.error_handler import handle_error

app = FastAPI()

@app.post("/generate-proposal")
def generate(lead: Lead):
        print("Request received")

        lead_data = lead.dict()
        print("Lead data:", lead_data)

        filename = create_proposal(lead_data)
        print("Generated:", filename)

        return {
            "status": "success",
            "filename": filename
        }



