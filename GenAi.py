# from deep_translator import GoogleTranslator
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, create_sql_query_chain

# Initialize reusable components outside the function
api_key = 'YOUR_KEY'
llm_model = ChatGroq(model="llama3-70b-8192", api_key=api_key)
# translator = GoogleTranslator()
db_uri = r"sqlite:///C:\Users\MYPC\OneDrive\Desktop\chatbot\chatbot_ui_lite\storage\DataBase.db"
db = SQLDatabase.from_uri(db_uri)

def extract_sql_query(template):
    answer_prompt = PromptTemplate(
 input_variables=["template"],
    template="""
You are a SQL query extractor. The input may or may not be a SQL query.

If the input is a meaningful SQL query, extract and return **only** the SQL query.

If the input does **not** contain a SQL query (e.g., greetings, thank you, etc.), return this exactly:

None

No explanation. Just output the query or the word "None".

Input: {template}

Answer:
"""
)

    llm_chain = LLMChain(llm=llm_model, prompt=answer_prompt)
    ans = llm_chain(inputs={"template": template})
    return ans["text"]

def Gen_Ai(questions):
  # Create and use the SQL query chain
    chain = create_sql_query_chain(llm_model, db)
    sql_query = chain.invoke({'question': questions})
    final_query = extract_sql_query(sql_query)
    if final_query.strip().lower() == "none":
        return sql_query, None    
     
    # Execute the SQL query
    try:
        result = db.run(final_query)
        result_text = '\n'.join(map(str, result))  # Ensure all results are included in the response
    except Exception as e:
        return f"Error executing SQL query: {e}", None

    # Generate response based on SQL result
    answer_prompt = PromptTemplate.from_template(
    """
    You are a friendly and helpful AI assistant. The user may ask questions in **any language**. You should:
    - **Understand** the question, even if it's not in English.
    - **Generate a SQL query internally** from that question.
    - **Respond back in the same language** that the user used to ask the question.
    
    Only use the SQL result to answer — do not show the SQL query or mention any databases.
    
    Always keep your answer natural, human-like, and informative. Be polite and helpful.
    
    User Question: {question}
    SQL Query: {query}
    SQL Result: {result}
    
    Your Response:
    """

    )
    llm_chain = LLMChain(llm=llm_model, prompt=answer_prompt)
    ans = llm_chain(inputs={"question": questions, "query": sql_query, "result": result_text})

    # # Translate the final answer back to the original language if needed
    final_answer = ans["text"]
    # if detected_language != 'en':
    #     final_answer = translator.translate(final_answer, source='en', target=detected_language)

    return final_answer, final_query
