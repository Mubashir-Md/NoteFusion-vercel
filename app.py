import pdfplumber
import openai
import PyPDF2
import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        file = request.files['pdf-file']
        readpdf = PyPDF2.PdfReader(file)
        totalpages = len(readpdf.pages)
        html = ""
        for i in range(2):
            with pdfplumber.open(file) as pdf:
                first_page = pdf.pages[i]
                x = first_page.extract_text()
            openai.api_key = os.getenv('API_KEY') 
            openai.api_base  = 'https://api.pawan.krd/v1'

            prop= x+  "These are the contents of a single page of a pdf.Identify the all topics and subtopics covered in this page using NLP techniques such as Named Entity Recognition and Topic Modeling. Generate a summary of the page by selecting the most important sentences and phrases related to the identified topics and subtopics. Create a concise summary of the page based on the selected sentences and phrases. The summary should be roughly based on all the contents of the page. Mention page numbers at the end of each page. The response must start with 'The summary of this page is: .....'. towards the end add a neatly formatted list of important keywords and creative pnemonics to help remember them in the exam."

            response = openai.Completion.create(

                model="gpt-3.5-turbo",
                prompt=prop,
                temperature=0.7,
                max_tokens=250,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
                )
            print(i)
         # finalop[i].append(response.choices[0].text)
            html += f"<div>Page {i+1}: {response.choices[0].text}</div>" # append the HTML for the current page to the overall HTML string
            x=""
        return html
    else:
        return render_template("index.html")
app.run()


