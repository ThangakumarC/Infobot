# from langchain_community.utilities.sql_database import SQLDatabase
# from langchain_groq import ChatGroq
# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain, create_sql_query_chain
# import re

# def extract_sql_query(template):
#     answer_prompt = PromptTemplate.from_template(

#         """you are a Sql_Query Extractor from noise string. Given the Noisy Sql template from that Exctract SQL query alone Dont give anything else. Just extract the Query and give it as an answer.

#     Noisy_query: {template}

#     Answer: """
#     )

#     llm_model = ChatGroq(model="llama3-70b-8192", api_key='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')
#     llm = LLMChain(llm=llm_model, prompt=answer_prompt)
#     ans = llm(inputs={"template": template})
#     print(ans["text"])
#     return ans["text"]

# def Gen_Ai(questions):
#     llm = ChatGroq(model="llama3-70b-8192", api_key='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')
#     db = SQLDatabase.from_uri(r"sqlite:///C:\Users\MYPC\OneDrive\Desktop\chatbot\chatbot_ui_lite\storage\DataBase.db")
#     chain = create_sql_query_chain(llm, db)
#     sql_query = chain.invoke({'question': questions})
#     final = extract_sql_query(sql_query)
#     result = db.run(final)

#     answer_prompt = PromptTemplate.from_template(
#         """Given the following user question, corresponding SQL query, and SQL result, generate a proper reply with proper structure to give to the user, don't give anything else except the answer.

#     Question: {question}
#     SQL Query: {query}
#     SQL Result: {result}

#     Answer: """
#     )

#     llm_model = ChatGroq(model="llama3-70b-8192", api_key='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')
#     llm = LLMChain(llm=llm_model, prompt=answer_prompt)
#     ans = llm(inputs={"question": questions, "query": sql_query, "result": result})
#     return ans["text"], final

#trans***
# from deep_translator import GoogleTranslator
# from langchain_community.utilities.sql_database import SQLDatabase
# from langchain_groq import ChatGroq
# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain, create_sql_query_chain

# def extract_sql_query(template):
#     answer_prompt = PromptTemplate.from_template(
#         """You are a SQL query extractor. Given the noisy SQL template, extract the SQL query alone. Don't give anything else. Just extract the query and provide it as an answer.

#         Noisy_query: {template}

#         Answer: """
#     )

#     llm_model = ChatGroq(model="llama3-70b-8192", api_key='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')
#     llm = LLMChain(llm=llm_model, prompt=answer_prompt)
#     ans = llm(inputs={"template": template})
#     return ans["text"]

# def Gen_Ai(questions):
#     translator = GoogleTranslator()
    
#     # Detect and translate input question to English
#     translated_question = translator.translate(questions, source='auto', target='en')

#     # Process the translated question
#     llm = ChatGroq(model="llama3-70b-8192", api_key='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')
#     db = SQLDatabase.from_uri(r"sqlite:///C:\Users\MYPC\OneDrive\Desktop\chatbot\chatbot_ui_lite\storage\DataBase.db")
#     chain = create_sql_query_chain(llm, db)
#     sql_query = chain.invoke({'question': translated_question})
#     final = extract_sql_query(sql_query)
#     result = db.run(final)

#     # Generate response with the SQL result
#     answer_prompt = PromptTemplate.from_template(
#         """Given the following user question, corresponding SQL query, and SQL result, generate a proper reply with a proper structure to give to the user. Don't give anything else except the answer.

#         Question: {question}
#         SQL Query: {query}
#         SQL Result: {result}

#         Answer: """
#     )

#     llm_model = ChatGroq(model="llama3-70b-8192", api_key='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')
#     llm = LLMChain(llm=llm_model, prompt=answer_prompt)
#     ans = llm(inputs={"question": questions, "query": sql_query, "result": result})

#     # Translate the final answer to the original language
#     final_answer = translator.translate(ans["text"], source='en', target='auto')
#     return final_answer, final

from deep_translator import GoogleTranslator
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, create_sql_query_chain

def extract_sql_query(template):
    answer_prompt = PromptTemplate.from_template(
        """You are a SQL query extractor. Given the noisy SQL template, extract the SQL query alone. Don't give anything else. Just extract the query and provide it as an answer.

        Noisy_query: {template}

        Answer: """
    )

    llm_model = ChatGroq(model="llama3-70b-8192", api_key='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')
    llm = LLMChain(llm=llm_model, prompt=answer_prompt)
    ans = llm(inputs={"template": template})
    return ans["text"]

def Gen_Ai(questions, detected_language='en'):
    translator = GoogleTranslator()

    # Detect and translate input question to English if needed
    if detected_language != 'en':
        translated_question = translator.translate(questions, source=detected_language, target='en')
    else:
        translated_question = questions

    # Process the translated question
    llm_model = ChatGroq(model="llama3-70b-8192", api_key='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')
    db = SQLDatabase.from_uri(r"sqlite:///C:\Users\MYPC\OneDrive\Desktop\chatbot\chatbot_ui_lite\storage\DataBase.db")
    chain = create_sql_query_chain(llm_model, db)
    sql_query = chain.invoke({'question': translated_question})
    final = extract_sql_query(sql_query)
    result = db.run(final)

    # Generate response with the SQL result
    answer_prompt = PromptTemplate.from_template(
        """Given the following user question, corresponding SQL query, and SQL result, generate a proper reply with a proper structure to give to the user. Don't give anything else except the answer.

        Question: {question}
        SQL Query: {query}
        SQL Result: {result}

        Answer: """
    )

    llm = LLMChain(llm=llm_model, prompt=answer_prompt)
    ans = llm(inputs={"question": questions, "query": sql_query, "result": result})

    # Translate the final answer back to the original language if needed
    if detected_language != 'en':
        final_answer = translator.translate(ans["text"], source='en', target=detected_language)
    else:
        final_answer = ans["text"]

    return final_answer, final

#trans
# from deep_translator import GoogleTranslator
# from langchain_community.utilities.sql_database import SQLDatabase
# from langchain_groq import ChatGroq
# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain, create_sql_query_chain

# def extract_sql_query(template):
#     answer_prompt = PromptTemplate.from_template(
#         """You are a SQL query extractor. Given the noisy SQL template, extract the SQL query alone. Don't give anything else. Just extract the query and provide it as an answer.

#         Noisy_query: {template}

#         Answer: """
#     )

#     llm_model = ChatGroq(model="llama3-70b-8192", api_key='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')
#     llm = LLMChain(llm=llm_model, prompt=answer_prompt)
#     ans = llm(inputs={"template": template})
#     return ans["text"]

# def Gen_Ai(question, detected_language='en'):
#     # Initialize the translator only if the language is not English
#     translator = GoogleTranslator() if detected_language != 'en' else None

#     # Translate the input question to English if necessary
#     if translator:
#         translated_question = translator.translate(question, source=detected_language, target='en')
#     else:
#         translated_question = question

#     # Process the translated question
#     llm = ChatGroq(model="llama3-70b-8192", api_key='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')
#     db = SQLDatabase.from_uri(r"sqlite:///C:\Users\MYPC\OneDrive\Desktop\chatbot\chatbot_ui_lite\storage\DataBase.db")
#     chain = create_sql_query_chain(llm, db)
#     sql_query = chain.invoke({'question': translated_question})
#     final = extract_sql_query(sql_query)
#     result = db.run(final)

#     # Generate response with the SQL result
#     answer_prompt = PromptTemplate.from_template(
#         """Given the following user question, corresponding SQL query, and SQL result, generate a proper reply with a proper structure to give to the user. Don't give anything else except the answer.

#         Question: {question}
#         SQL Query: {query}
#         SQL Result: {result}

#         Answer: """
#     )

#     llm_model = ChatGroq(model="llama3-70b-8192", api_key='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')
#     llm = LLMChain(llm=llm_model, prompt=answer_prompt)
#     ans = llm(inputs={"question": question, "query": sql_query, "result": result})

#     # Translate the final answer back to the original language if necessary
#     final_answer = translator.translate(ans["text"], source='en', target=detected_language) if translator else ans["text"]
#     return final_answer, final
#next

# from deep_translator import GoogleTranslator
# from langchain_community.utilities.sql_database import SQLDatabase
# from langchain_groq import ChatGroq
# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain, create_sql_query_chain

# def extract_sql_query(template):
#     answer_prompt = PromptTemplate.from_template(
#         """You are a SQL query extractor. Given the noisy SQL template, extract the SQL query alone. Don't give anything else. Just extract the query and provide it as an answer.

#         Noisy_query: {template}

#         Answer: """
#     )

#     llm_model = ChatGroq(model="llama3-70b-8192", api_key='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')
#     llm = LLMChain(llm=llm_model, prompt=answer_prompt)
#     ans = llm(inputs={"template": template})
#     return ans["text"]

# def Gen_Ai(questions, detected_language=None):
#     translator = GoogleTranslator()
    
#     # Detect and translate input question to English
#     translated_question = translator.translate(questions, source=detected_language or 'auto', target='en')

#     # Process the translated question
#     llm = ChatGroq(model="llama3-70b-8192", api_key='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')
#     db = SQLDatabase.from_uri(r"sqlite:///C:\Users\MYPC\OneDrive\Desktop\chatbot\chatbot_ui_lite\storage\DataBase.db")
#     chain = create_sql_query_chain(llm, db)
#     sql_query = chain.invoke({'question': translated_question})
#     final = extract_sql_query(sql_query)
#     result = db.run(final)

#     # Generate response with the SQL result
#     answer_prompt = PromptTemplate.from_template(
#         """Given the following user question, corresponding SQL query, and SQL result, generate a proper reply with a proper structure to give to the user. Don't give anything else except the answer.

#         Question: {question}
#         SQL Query: {query}
#         SQL Result: {result}

#         Answer: """
#     )

#     llm_model = ChatGroq(model="llama3-70b-8192", api_key='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')
#     llm = LLMChain(llm=llm_model, prompt=answer_prompt)
#     ans = llm(inputs={"question": questions, "query": sql_query, "result": result})

#     # Translate the final answer to the original language
#     final_answer = translator.translate(ans["text"], source='en', target=detected_language or 'en')
#     return final_answer, final




#trans2.0
# from googletrans import Translator
# from langchain_community.utilities.sql_database import SQLDatabase
# from langchain_groq import ChatGroq
# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain, create_sql_query_chain

# def extract_sql_query(template):
#     answer_prompt = PromptTemplate.from_template(
#         """You are a SQL query extractor. Given the noisy SQL template, extract the SQL query alone. Don't give anything else. Just extract the query and provide it as an answer.

#         Noisy_query: {template}

#         Answer: """
#     )

#     llm_model = ChatGroq(model="llama3-70b-8192", api_key='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')
#     llm = LLMChain(llm=llm_model, prompt=answer_prompt)
#     ans = llm(inputs={"template": template})
#     return ans["text"]

# def Gen_Ai(questions):
#     translator = Translator()

#     # Detect and translate input question to English
#     translated_question = translator.translate(questions, dest='en').text

#     # Process the translated question
#     llm = ChatGroq(model="llama3-70b-8192", api_key='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')
#     db = SQLDatabase.from_uri(r"sqlite:///C:\Users\MYPC\OneDrive\Desktop\chatbot\chatbot_ui_lite\storage\DataBase.db")
#     chain = create_sql_query_chain(llm, db)
#     sql_query = chain.invoke({'question': translated_question})
#     final = extract_sql_query(sql_query)
#     result = db.run(final)

#     # Generate response with the SQL result
#     answer_prompt = PromptTemplate.from_template(
#         """Given the following user question, corresponding SQL query, and SQL result, generate a proper reply with a proper structure to give to the user. Don't give anything else except the answer.

#         Question: {question}
#         SQL Query: {query}
#         SQL Result: {result}

#         Answer: """
#     )

#     llm_model = ChatGroq(model="llama3-70b-8192", api_key='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')
#     llm = LLMChain(llm=llm_model, prompt=answer_prompt)
#     ans = llm(inputs={"question": questions, "query": sql_query, "result": result})

#     # Translate the final answer to the original language
#     final_answer = translator.translate(ans["text"], dest='auto').text
#     return final_answer, final

#4
# from deep_translator import GoogleTranslator
# import openai

# # Set your OpenAI API key
# openai.api_key = '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'

# # Function to translate text to a target language
# def translate_text(text, target_lang='en'):
#     translator = GoogleTranslator(source='auto', target=target_lang)
#     translated_text = translator.translate(text)
#     return translated_text

# # Function to generate AI responses
# def Gen_Ai(questions):
#     # First, translate the user's question to English
#     translated_question = translate_text(questions, target_lang='en')
    
#     # Generate the AI response using the translated question
#     response = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=translated_question,
#         max_tokens=150
#     )

#     # Translate the AI's response back to the original language
#     final_answer = translate_text(response.choices[0].text.strip(), target_lang='auto')
#     return final_answer


#5th

# from gtts import gTTS
# from io import BytesIO
# import textwrap
# from transformers import pipeline
# import sqlite3  # Example for SQLite, adjust as needed

# def translate_text(text, target_language):
#     translator = pipeline("translation", model=f"Helsinki-NLP/opus-mt-en-{target_language}")
#     return translator(text)[0]['translation_text']

# def extract_sql_query(template):
#     # Example extraction logic, replace with actual logic
#     return f"SELECT * FROM users WHERE name LIKE '%{template}%'"

# def Gen_Ai(questions):
#     # Translate the question to English if needed
#     translated_question = translate_text(questions, "en")
    
#     # Generate SQL query and get the result from the database
#     sql_query = extract_sql_query(translated_question)
    
#     # Example connection to SQLite database (replace with your DB)
#     conn = sqlite3.connect('example.db')
#     cursor = conn.cursor()
#     cursor.execute(sql_query)
#     result = cursor.fetchall()
    
#     # Translate the result back to the original language
#     final_answer = translate_text(str(result), "auto")
#     conn.close()
#     return final_answer, sql_query

# def synthesize_speech(text, file_path):
#     # Convert text to speech and save it as an MP3 file
#     tts = gTTS(text, lang='en')  # Set the language code as needed
#     tts.save(file_path)
