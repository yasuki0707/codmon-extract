from dotenv import load_dotenv
load_dotenv()

import os

CODMON_EMAIL = os.getenv('CODMON_EMAIL')
CODMON_PASSWORD = os.getenv('CODMON_PASSWORD')

