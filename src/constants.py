import os
from openai import OpenAI
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

client = OpenAI()

# Import Models
model = os.environ.get("GPT_MODEL")

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Import DB url
MONGO_URI = os.environ.get("MONGO_URI")

# JWT token
API_KEY = os.environ.get("API-KEY")