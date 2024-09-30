from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


# Configura el modelo de Ollama (Llama3)
llm = Ollama(model='llama3:8b')

# Define el template del prompt para el modelo
prompt_template = PromptTemplate(
    input_variables=['personal_information'],
    template="""
    You are a virtual assistant in charge of extracting information from this text: {personal_information}.
    
    Your task will be to extract data such as:
    1. The ID number of the document; make sure you do not confuse the ID number with another number given in the text.
    2. The full name of the person (first name, middle name if any, and all last names) where the first letter of each first or last name is capitalized and the other letters of the name are lowercase.
    3. The person's date of birth in format: YYYYY-MM-DD.
    4. Place of birth in format: City (Department).
    5. Exclusively the date on which the document was issued in format: YYYYY-MM-DD. Appears near the "lugar de expedición".
    6. Exclusively the place where the document was issued in format: City (Department). Appears near the "fecha de expedición".

    Please note that due to typing errors the information related to Colombian place names may be incorrectly filled in, so if you see that the names do not match with cities and departments of Colombia, please correct them.

    Remember to return me the answer in Spanish and in 6 paragraphs where each paragraph corresponds to each step previously indicated only with the requested answer and without any explanation of what each answer corresponds to. If you can't find something in the text, please respond: 'No encontrado'.
    """
)

# Crea la cadena LLM
chain = LLMChain(llm=llm, prompt=prompt_template)

def answer_question(personal_information: str) -> str:
    # Obtiene la respuesta del modelo usando invoke
    extraction_data = chain.invoke({'personal_information': personal_information})
    return extraction_data.get('text')

if __name__ == '__main__':
    while True:
        row_data = input(
            'Ingrese el texto al que desea extraerle la información (escriba "salir" para terminar):\n'
            )
        if row_data.lower() == 'salir':
            break
        answer = answer_question(row_data)
        print(f'{answer}\n__\n')
