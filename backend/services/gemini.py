import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# ✅ Configure the correct API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# ✅ Use the full model name, this now works with v1
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_response(prompt):
    response = model.generate_content(prompt)
    return response.text
