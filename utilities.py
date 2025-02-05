# imports
import os
from dotenv import load_dotenv
from openai import OpenAI

from IPython.display import Markdown, display, update_display

# Load environment variables in a file called .env
# Print the key prefixes to help with any debugging

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')


if openai_api_key:
    print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
    print("OpenAI API Key not set")
    

# Connect to OpenAI

openai = OpenAI() #Connect the API for the first bot
openai2 = OpenAI() #Connect the API for the second bot


gpt_model = "gpt-4o-mini"


gpt_system = "You are a chatbot that discusses politics but never find a common ground with your discussion partner"

gpt_system2 = "You are a chatbot that discusses politics but tries to find a common ground with your discussion partner"

gpt_messages = ["Hi there"]
gpt_messages2 = ["Hi"]