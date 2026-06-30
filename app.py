from fastapi import FastAPI
from fastapi.responses import FileResponse
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

    return FileResponse(
        path=str(filename),
        filename=filename.name,
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )



