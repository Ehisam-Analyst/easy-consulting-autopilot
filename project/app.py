from repositories.lead_repository import create_lead
from fastapi import FastAPI
from fastapi.responses import FileResponse
from project.models import Lead
from services.proposal_service import create_proposal
from project.error_handler import handle_error
from fastapi import Depends
from sqlalchemy.orm import Session
from project.database import get_db

app = FastAPI()

@app.post("/generate-proposal")
def generate(lead: Lead,
             db: Session = Depends(get_db)
             ):
    print("Request received")

    lead_data = lead.dict()
    result = create_proposal(db, lead_data)
    filename = result["filename"]

    return FileResponse(
    path=str(filename),
    filename=filename.name,
    )



