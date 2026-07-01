from pydantic import BaseModel
class Lead(BaseModel):

    company: str
    industry: str
    country: str
    service: str

leads = {
        "company": "ABC Bank",
        "industry": "Banking",
        "country": "USA",
        "service": "Consulting"
    }
