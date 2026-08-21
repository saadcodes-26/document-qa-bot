from google import genai
from pypdf import PdfReader
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("your_API_KEY")

pdf_file = ("")

if not os.path.exists(pdf_file):
    print("Error: No Pdf file found")
else:


 reader = PdfReader("")
 notes = ""
 for page in reader.pages:
    notes += page.extract_text()

 chat = client.chats.create(
    model="gemini-3.6-flash"
)

while True:
    question = input("How can i help you?\n ")
    if question == "quit":
       break
    
    prompt = f"Based on this Texts:\n\n{notes}\n\n Answer this question{question}"
    try:
       
     response = chat.send_message(prompt)
     print("AI: " ,response.text)

    except Exception as e:
       print("Something went wrong, try again:", e)
