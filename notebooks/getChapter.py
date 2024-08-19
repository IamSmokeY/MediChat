import groq
import dotenv
import os
from PyPDF2 import PdfReader
dotenv.load_dotenv()

client = groq.Client(api_key=os.getenv('GROQ_API_KEY'))
current_path = os.path.abspath(__file__)

def _load_index(path):
    reader = PdfReader(path)
    print()
    pdf_content = ""
    for page in reader.pages:
        pdf_content += page.extract_text() + "\n"
    return pdf_content.strip()
index = _load_index(os.path.join(os.path.dirname(current_path), "book", "index.pdf"))



def _getMessages(question):
    messages=[
            {
                "role": "user",
                "content": "Given a question and index of a book, specify which chapter does the question belong to. If there is any ambiguity, clarify with the user."
            },
            {
                "role": "system",
                "content": "Sure, provide me with the question and the index of the book."
            },
            {
                "role": "user",
                "content": f"The index of the book is \n{index}"
            },
            {
                "role": "system",
                "content": f"Please ask a question, and I will respond with the lesson that the question pertains to."
            },
            {
                "role": "user",
                "content": f"The question is \n{question}"
            },
    ]
    return messages

def getChapter(question):
    messages = _getMessages(question)
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        temperature=0.5,
        max_tokens=1000
    )
    return response.choices[0].message.content

print(getChapter("What is metabolism?"))




