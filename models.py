from pydantic import BaseModel
class Lead(BaseModel):

    company: str
    industry: str

leads = {
        "company": "ABC Bank",
        "industry": "Banking"
    }
