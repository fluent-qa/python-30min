

import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
DOMAIN = os.environ["DOMAIN"]
PROJECT_NAME=os.environ["PROJECT_NAME"]

print(f"{DOMAIN},{PROJECT_NAME}")
