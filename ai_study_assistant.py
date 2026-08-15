from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

print("AI Study Assistant")
print("Your AI assistant is ready!")