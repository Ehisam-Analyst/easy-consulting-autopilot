
from docxtpl import DocxTemplate
from datetime import date
from docx2pdf import convert
from config import TEMPLATE_FILE, OUTPUT_DIR

template = DocxTemplate(str(TEMPLATE_FILE))


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
    filename = OUTPUT_DIR / f"{lead['company']}_Proposal.docx"   
    template.save( filename
        
    )
    filename_pdf =  f"output/{lead['company']}_Proposal.pdf"
    convert(filename, filename_pdf)
    
    print("Generating Proposal...")

    return filename_pdf