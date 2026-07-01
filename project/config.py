from pathlib import Path

BASE_DIR = Path(__file__).parent

TEMPLATE_DIR = BASE_DIR / "templates"
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

TEMPLATE_FILE = TEMPLATE_DIR / "RegTech365_Proposal_Template.docx"