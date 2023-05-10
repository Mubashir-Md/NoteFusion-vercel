import pdfplumber
import openai
with pdfplumber.open("Unit-1.pdf") as pdf:
    first_page = pdf.pages[0]
    x = first_page.extract_text()
openai.api_key = 'pk-YspeKZWeIktTmWZKtXEPtisBOuORiPbcaJcRAfIaaCvPCekg'
openai.api_base  = 'https://api.pawan.krd/v1'

prop= x+  "Instructions: Compose a comprehensive reply to the query using the search results given. "\
              "Cite each reference using [ Page Number] notation (every result has this number at the beginning). "\
              "Citation stransformershould be done at the end of each sentence. If the search results mention multiple subjects "\
              "with the same name, create separate answers for each. Only include information found in the results and "\
              "don't add any additional information. Make sure the answer is correct and don't output false content. "\
              "If the text does not relate to the query, simply state 'Text Not Found in PDF'. Ignore outlier "\
              "search results which has nothing to do with the question. Only answer what is asked. The "\
              "answer should be short and concise. Answer step-by-step. \n\nQuery: {question}\nAnswer: "

response = openai. Completion.create(

    model="gpt-3.5-turbo",
    prompt=prop,
    temperature=0.7,
    max_tokens=1000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    )
print (response.choices[0].text)