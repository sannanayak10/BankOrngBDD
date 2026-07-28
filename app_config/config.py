from pathlib import Path
from dotenv import load_dotenv
import os
import dr

ROOT = Path(__file__).parent.parent
load_dotenv(ROOT / '.env')


BROWSER = os.getenv('BROWSER', 'chromium')
HEADLESS = os.getenv('HEADLESS', 'True') == 'True'
