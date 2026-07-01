
from docxtpl import DocxTemplate
from datetime import date
from datetime import datetime
from project.config import TEMPLATE_FILE, OUTPUT_DIR

template = DocxTemplate(str(TEMPLATE_FILE))
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")


today = date.today()
def generate_proposal(lead):
    template = DocxTemplate(
            "templates/RegTech365_Proposal_Template.docx"
    )
    context = {
        "organization_name": lead["company"],
        "date": today,
    }
    template.render(context)
    filename = OUTPUT_DIR / f"{lead['company']}_{timestamp}_Proposal.docx"   
    template.save( filename
    )
    return filename