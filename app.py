# import os
# import sqlite3
# import pandas as pd
# from csv_db import CSV_2_DB
# from GenAi import Gen_Ai
# import streamlit as st
# import speech_recognition as sr
# from gtts import gTTS
# from deep_translator import GoogleTranslator
# from langdetect import detect, LangDetectException
# from groq import Groq

# # Initialize Groq client with your API key
# api_key = "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"
# client = Groq(api_key=api_key)

# def play_audio(text, lang='en'):
#     try:
#         # Convert text to speech and save it to a file
#         tts = gTTS(text=text, lang=lang)
#         audio_file = "temp_audio.mp3"
#         tts.save(audio_file)
        
#         # Read the audio file and display it in Streamlit
#         with open(audio_file, "rb") as f:
#             audio_bytes = f.read()
#             st.audio(audio_bytes, format='audio/mp3')

#         # Optionally, delete the file after usage
#         os.remove(audio_file)
#     except Exception as e:
#         st.error(f"Error generating audio: {e}")

# def detect_language(text):
#     try:
#         return detect(text)
#     except LangDetectException:
#         return 'en'
#     except Exception as e:
#         st.error(f"Error detecting language: {e}")
#         return 'en'

# def translate_text(text, source_lang='en', target_lang='en'):
#     try:
#         translator = GoogleTranslator(source=source_lang, target=target_lang)
#         return translator.translate(text)
#     except Exception as e:
#         st.error(f"Error translating text: {e}")
#         return text

# def transcribe_audio_with_groq(file_path, language='ta'):
#     try:
#         with open(file_path, "rb") as file:
#             transcription = client.audio.transcriptions.create(
#                 file=(os.path.basename(file_path), file.read()),  # Provide filename and file content
#                 model="whisper-large-v3",
#                 prompt="Specify context or spelling",  # Optional
#                 response_format="json",  # Optional
#                 language=language,  # Language code
#                 temperature=0.0  # Optional
#             )
#         return transcription.text
#     except Exception as e:
#         st.error(f"Error during transcription: {e}")
#         return ""

# def main():
#     st.title("InfoBot")

#     with st.sidebar:
#         st.subheader("Upload CSV Files")
#         uploaded_files = st.file_uploader("Upload CSV files", accept_multiple_files=True)
#         if uploaded_files:
#             for uploaded_file in uploaded_files:
#                 file_path = os.path.join("storage", uploaded_file.name)
#                 with open(file_path, "wb") as f:
#                     f.write(uploaded_file.getbuffer())
#             CSV_2_DB()
#             st.write(":green[DB created]")

#     # Provide options for text or voice input
#     input_mode = st.radio("Choose input mode", ("Text", "Voice"))

#     if input_mode == "Text":
#         user_query = st.text_input("Enter your query", key="query_input")
#         detected_language = detect_language(user_query)
#         st.write(f"Detected Language: {detected_language}")

#         # Translate to English for query processing
#         translated_query = translate_text(user_query, source_lang=detected_language, target_lang='en')

#     elif input_mode == "Voice":
#         if st.button("Record Voice Query"):
#             recognizer = sr.Recognizer()
#             with sr.Microphone() as source:
#                 st.write("Listening...")
#                 audio = recognizer.listen(source)
#                 try:
#                     audio_file_path = "temp_audio.wav"
#                     with open(audio_file_path, "wb") as audio_file:
#                         audio_file.write(audio.get_wav_data())

#                     # Transcribe the recorded audio using Groq
#                     transcription_text = transcribe_audio_with_groq(audio_file_path, language='ta')
#                     st.write(f"Recorded Query: {transcription_text}")

#                     # Detect language from the transcribed text
#                     detected_language = detect_language(transcription_text)
#                     st.write(f"Detected Language: {detected_language}")

#                     # Translate to English for query processing
#                     translated_query = translate_text(transcription_text, source_lang=detected_language, target_lang='en')

#                 except sr.UnknownValueError:
#                     st.error("Sorry, I could not understand the audio.")
#                     return
#                 except sr.RequestError:
#                     st.error("Sorry, there was an issue with the speech recognition service.")
#                     return
#         else:
#             st.warning("Click 'Record Voice Query' to start recording.")

#     if 'user_query' in locals() or (input_mode == "Voice" and 'transcription_text' in locals()):
#         try:
#             result, query = Gen_Ai(translated_query, detected_language)

#             # Translate the result back to the original language
#             final_result = translate_text(result, source_lang='en', target_lang=detected_language)
            
#             st.write(f"SQL Query: {query}")
#             st.write(f":green[{final_result}]")

#             # Convert the result to speech and play it
#             play_audio(final_result, lang=detected_language)
#         except Exception as e:
#             st.error(f"Error: {e}")

# if __name__ == "__main__":
#     main()



# import os
# import sqlite3
# import pandas as pd
# from csv_db import CSV_2_DB
# from GenAi import Gen_Ai
# import streamlit as st
# import speech_recognition as sr
# from gtts import gTTS
# from deep_translator import GoogleTranslator
# from langdetect import detect, LangDetectException

# def play_audio(text, lang='en'):
#     try:
#         # Convert text to speech and save it to a file
#         tts = gTTS(text=text, lang=lang)
#         audio_file = "temp_audio.mp3"
#         tts.save(audio_file)
        
#         # Read the audio file and display it in Streamlit
#         with open(audio_file, "rb") as f:
#             audio_bytes = f.read()
#             st.audio(audio_bytes, format='audio/mp3')

#         # Optionally, delete the file after usage
#         os.remove(audio_file)
#     except Exception as e:
#         st.error(f"Error generating audio: {e}")

# def detect_language(text):
#     try:
#         return detect(text)
#     except LangDetectException:
#         return 'en'
#     except Exception as e:
#         st.error(f"Error detecting language: {e}")
#         return 'en'

# def translate_text(text, source_lang='en', target_lang='en'):
#     try:
#         translator = GoogleTranslator(source=source_lang, target=target_lang)
#         return translator.translate(text)
#     except Exception as e:
#         st.error(f"Error translating text: {e}")
#         return text

# def main():
#     st.title("InfoBot")

#     with st.sidebar:
#         st.subheader("Upload CSV Files")
#         uploaded_files = st.file_uploader("Upload CSV files", accept_multiple_files=True)
#         if uploaded_files:
#             for uploaded_file in uploaded_files:
#                 file_path = os.path.join(r"C:\Users\MYPC\OneDrive\Desktop\chatbot\chatbot_ui_lite\storage", uploaded_file.name)
#                 with open(file_path, "wb") as f:
#                     f.write(uploaded_file.getbuffer())
#             CSV_2_DB()
#             st.write(":green[DB created]")

#     user_query = st.text_input("Enter your query", key="query_input")

#     if st.button("Record Voice Query"):
#         recognizer = sr.Recognizer()
#         with sr.Microphone() as source:
#             st.write("Listening...")
#             audio = recognizer.listen(source)
#             try:
#                 user_query = recognizer.recognize_google(audio)
#                 st.write(f"Recorded Query: {user_query}")

#                 # Detect language from the voice input
#                 detected_language = detect_language(user_query)
#                 st.write(f"Detected Language: {detected_language}")

#                 # Translate to English for query processing
#                 translated_query = translate_text(user_query, source_lang=detected_language, target_lang='en')

#             except sr.UnknownValueError:
#                 st.error("Sorry, I could not understand the audio.")
#                 return
#             except sr.RequestError:
#                 st.error("Sorry, there was an issue with the speech recognition service.")
#                 return
#     else:
#         detected_language = detect_language(user_query)
#         translated_query = translate_text(user_query, source_lang=detected_language, target_lang='en')

#     if user_query:
#         try:
#             result, query = Gen_Ai(translated_query, detected_language)

#             # Translate the result back to the original language
#             final_result = translate_text(result, source_lang='en', target_lang=detected_language)
            
#             st.write(f"SQL Query : {query}")
#             st.write(f":green[{final_result}]")

#             # Convert the result to speech and play it
#             play_audio(final_result, lang=detected_language)
#         except Exception as e:
#             st.error(f"Error: {e}")

# if __name__ == "__main__":
#     main()

# import os
# import sqlite3
# import speech_recognition as sr
# from gtts import gTTS
# from deep_translator import GoogleTranslator
# import vosk
# import json

# # Load Vosk model for speech recognition
# def load_vosk_model(model_path):
#     try:
#         model = vosk.Model(model_path)
#         return model
#     except Exception as e:
#         print(f"Error loading Vosk model: {e}")
#         return None

# # Transcribe audio with Vosk
# def transcribe_audio_with_vosk(audio_path, model):
#     rec = vosk.KaldiRecognizer(model, 16000)
#     with open(audio_path, "rb") as audio_file:
#         audio_data = audio_file.read()
#     rec.AcceptWaveform(audio_data)
#     result = json.loads(rec.Result())
#     return result.get('text', '')

# # Detect and translate text
# def translate_text(text, target_language='en'):
#     translator = GoogleTranslator()
#     return translator.translate(text, target=target_language)

# # Convert text to speech
# def text_to_speech(text, lang='en'):
#     tts = gTTS(text=text, lang=lang)
#     audio_path = "output.mp3"
#     tts.save(audio_path)
#     os.system(f"start {audio_path}")

# # Query SQLite database
# def query_database(query):
#     # Corrected file path
#     conn = sqlite3.connect(r'C:\Users\MYPC\OneDrive\Desktop\chatbot\chatbot_ui_lite\storage\DataBase.db')
#     cursor = conn.cursor()
#     cursor.execute(query)
#     result = cursor.fetchall()
#     conn.close()
#     return result

# # Main function to handle user input
# def main():
#     # Paths to the models
#     # Corrected path
#     vosk_model_path = r"C:\Users\MYPC\OneDrive\Desktop\chatbot\chatbot_ui_lite\vosk_model"
#     vosk_model = load_vosk_model(vosk_model_path)

#     # Record audio or use existing audio file
#     audio_path = "input.wav"  # Update with your audio file path

#     # Transcribe audio
#     text = transcribe_audio_with_vosk(audio_path, vosk_model)
#     print(f"Transcribed Text: {text}")

#     # Translate text if needed (e.g., from non-English to English)
#     translated_text = translate_text(text, target_language='en')
#     print(f"Translated Text: {translated_text}")

#     # Query the database
#     query = f"SELECT * FROM your_table WHERE your_column='{translated_text}'"  # Update with your query
#     query_result = query_database(query)
#     response = str(query_result)
#     print(f"Query Result: {response}")

#     # Convert response to speech
#     text_to_speech(response)

# if __name__ == "__main__":
#     main()

# import os
# import sqlite3
# import pandas as pd
# from csv_db import CSV_2_DB
# from GenAi import Gen_Ai
# import streamlit as st

# def main():
#     st.title("InfoBot")

#     with st.sidebar:
#         st.subheader("Upload CSV Files")
#         uploaded_files = st.file_uploader("Upload CSV files", accept_multiple_files=True)
#         if uploaded_files:
#             st.write(":green[DB created]")
   
#     # col1, col2, col3 = st.columns([1, 2, 1])
    
#     user_query = st.text_input("Enter your query", key="query_input")

#     if uploaded_files:
#         for uploaded_file in uploaded_files:
#             file_path = os.path.join(r"C:\Users\MYPC\OneDrive\Desktop\chatbot\chatbot_ui_lite\storage", uploaded_file.name)
#             with open(file_path, "wb") as f:
#                 f.write(uploaded_file.getbuffer())

#         CSV_2_DB()
        

#     if user_query:
#         try:
#             result, query = Gen_Ai(user_query)
#             st.write(f"SQL Query : {query}")
#             st.write(f":green[{result}]")
#         except Exception as e:
#             st.error(f"Error: {e}")

# if __name__ == "__main__":
#     main()

#voice

# import os
# import sqlite3
# import pandas as pd
# from csv_db import CSV_2_DB
# from GenAi import Gen_Ai
# import streamlit as st
# import speech_recognition as sr
# from gtts import gTTS
# from langdetect import detect
# from io import BytesIO

# def play_audio(audio_data):
#     audio_bytes = BytesIO()
#     audio_data.write_to_file(audio_bytes)
#     audio_bytes.seek(0)
#     audio_base64 = base64.b64encode(audio_bytes.getvalue()).decode()
#     st.audio(audio_base64, format='audio/wav')

# def detect_language(text):
#     try:
#         return detect(text)
#     except:
#         return 'en'

# def main():
#     st.title("InfoBot")

#     with st.sidebar:
#         st.subheader("Upload CSV Files")
#         uploaded_files = st.file_uploader("Upload CSV files", accept_multiple_files=True)
#         if uploaded_files:
#             st.write(":green[DB created]")

#     user_query = st.text_input("Enter your query", key="query_input")

#     if st.button("Record Voice Query"):
#         recognizer = sr.Recognizer()
#         with sr.Microphone() as source:
#             st.write("Listening...")
#             audio = recognizer.listen(source)
#             try:
#                 user_query = recognizer.recognize_google(audio)
#                 st.write(f"Recorded Query: {user_query}")

#                 # Detect language from the voice input
#                 detected_language = detect_language(user_query)
#                 st.write(f"Detected Language: {detected_language}")

#             except sr.UnknownValueError:
#                 st.error("Sorry, I could not understand the audio.")
#                 return
#             except sr.RequestError:
#                 st.error("Sorry, there was an issue with the speech recognition service.")
#                 return
#     else:
#         detected_language = detect_language(user_query)

#     if uploaded_files:
#         for uploaded_file in uploaded_files:
#             file_path = os.path.join(r"C:\Users\MYPC\OneDrive\Desktop\chatbot\chatbot_ui_lite\storage", uploaded_file.name)
#             with open(file_path, "wb") as f:
#                 f.write(uploaded_file.getbuffer())
#         CSV_2_DB()

#     if user_query:
#         try:
#             result, query = Gen_Ai(user_query, original_language=detected_language)
#             st.write(f"SQL Query : {query}")
#             st.write(f":green[{result}]")

#             # Convert the result to speech and play it
#             tts = gTTS(text=result, lang=detected_language)
#             play_audio(tts)
#         except Exception as e:
#             st.error(f"Error: {e}")

# if __name__ == "__main__":
#     main()

#voice***

# import os
# import sqlite3
# import pandas as pd
# from csv_db import CSV_2_DB
# from GenAi import Gen_Ai
# import streamlit as st
# import speech_recognition as sr
# from gtts import gTTS
# from langdetect import detect
# from io import BytesIO
# import base64

# def play_audio(text, lang='en'):
#     # Convert text to speech and save it to a file
#     tts = gTTS(text=text, lang=lang)
#     audio_file = "temp_audio.mp3"
#     tts.save(audio_file)
    
#     # Read the audio file and display it in Streamlit
#     with open(audio_file, "rb") as f:
#         audio_bytes = f.read()
#         st.audio(audio_bytes, format='audio/mp3')

# def detect_language(text):
#     try:
#         return detect(text)
#     except:
#         return 'en'

# def main():
#     st.title("InfoBot")

#     with st.sidebar:
#         st.subheader("Upload CSV Files")
#         uploaded_files = st.file_uploader("Upload CSV files", accept_multiple_files=True)
#         if uploaded_files:
#             st.write(":green[DB created]")

#     user_query = st.text_input("Enter your query", key="query_input")

#     if st.button("Record Voice Query"):
#         recognizer = sr.Recognizer()
#         with sr.Microphone() as source:
#             st.write("Listening...")
#             audio = recognizer.listen(source)
#             try:
#                 user_query = recognizer.recognize_google(audio)
#                 st.write(f"Recorded Query: {user_query}")

#                 # Detect language from the voice input
#                 detected_language = detect_language(user_query)
#                 st.write(f"Detected Language: {detected_language}")

#             except sr.UnknownValueError:
#                 st.error("Sorry, I could not understand the audio.")
#                 return
#             except sr.RequestError:
#                 st.error("Sorry, there was an issue with the speech recognition service.")
#                 return
#     else:
#         detected_language = detect_language(user_query)

#     if uploaded_files:
#         for uploaded_file in uploaded_files:
#             file_path = os.path.join(r"C:\Users\MYPC\OneDrive\Desktop\chatbot\chatbot_ui_lite\storage", uploaded_file.name)
#             with open(file_path, "wb") as f:
#                 f.write(uploaded_file.getbuffer())
#         CSV_2_DB()

#     if user_query:
#         try:
#             result, query = Gen_Ai(user_query, detected_language)
#             st.write(f"SQL Query : {query}")
#             st.write(f":green[{result}]")

#             # Convert the result to speech and play it
#             play_audio(result, lang=detected_language)
#         except Exception as e:
#             st.error(f"Error: {e}")

# if __name__ == "__main__":
#     main()


# import os
# import sqlite3
# import pandas as pd
# from csv_db import CSV_2_DB
# from GenAi import Gen_Ai
# import streamlit as st
# import speech_recognition as sr
# from gtts import gTTS
# from langdetect import detect, LangDetectException

# def play_audio(text, lang='en'):
#     try:
#         # Convert text to speech and save it to a file
#         tts = gTTS(text=text, lang=lang)
#         audio_file = "temp_audio.mp3"
#         tts.save(audio_file)
        
#         # Read the audio file and display it in Streamlit
#         with open(audio_file, "rb") as f:
#             audio_bytes = f.read()
#             st.audio(audio_bytes, format='audio/mp3')

#         # Optionally, delete the file after usage
#         os.remove(audio_file)
#     except Exception as e:
#         st.error(f"Error generating audio: {e}")

# def detect_language(text):
#     try:
#         return detect(text)
#     except LangDetectException:
#         return 'en'
#     except Exception as e:
#         st.error(f"Error detecting language: {e}")
#         return 'en'

# def main():
#     st.title("InfoBot")

#     with st.sidebar:
#         st.subheader("Upload CSV Files")
#         uploaded_files = st.file_uploader("Upload CSV files", accept_multiple_files=True)
#         if uploaded_files:
#             for uploaded_file in uploaded_files:
#                 file_path = os.path.join(r"C:\Users\MYPC\OneDrive\Desktop\chatbot\chatbot_ui_lite\storage", uploaded_file.name)
#                 with open(file_path, "wb") as f:
#                     f.write(uploaded_file.getbuffer())
#             CSV_2_DB()
#             st.write(":green[DB created]")

#     user_query = st.text_input("Enter your query", key="query_input")

#     if st.button("Record Voice Query"):
#         recognizer = sr.Recognizer()
#         with sr.Microphone() as source:
#             st.write("Listening...")
#             audio = recognizer.listen(source)
#             try:
#                 user_query = recognizer.recognize_google(audio)
#                 st.write(f"Recorded Query: {user_query}")

#                 # Detect language from the voice input
#                 detected_language = detect_language(user_query)
#                 st.write(f"Detected Language: {detected_language}")

#             except sr.UnknownValueError:
#                 st.error("Sorry, I could not understand the audio.")
#                 return
#             except sr.RequestError:
#                 st.error("Sorry, there was an issue with the speech recognition service.")
#                 return
#     else:
#         detected_language = detect_language(user_query)

#     if user_query:
#         try:
#             result, query = Gen_Ai(user_query, detected_language)
#             st.write(f"SQL Query : {query}")
#             st.write(f":green[{result}]")

#             # Convert the result to speech and play it
#             play_audio(result, lang=detected_language)
#         except Exception as e:
#             st.error(f"Error: {e}")

# if __name__ == "__main__":
#     main()


#main..............

# import os
# import sqlite3
# import pandas as pd
# from csv_db import CSV_2_DB
# from GenAi import Gen_Ai
# import streamlit as st
# import speech_recognition as sr
# from gtts import gTTS
# from langdetect import detect, LangDetectException

# def play_audio(text, lang='en'):
#     try:
#         # Convert text to speech and save it to a file
#         tts = gTTS(text=text, lang=lang)
#         audio_file = "temp_audio.mp3"
#         tts.save(audio_file)
        
#         # Read the audio file and display it in Streamlit
#         with open(audio_file, "rb") as f:
#             audio_bytes = f.read()
#             st.audio(audio_bytes, format='audio/mp3')

#         # Optionally, delete the file after usage
#         os.remove(audio_file)
#     except Exception as e:
#         st.error(f"Error generating audio: {e}")

# def detect_language(text):
#     try:
#         return detect(text)
#     except LangDetectException:
#         return 'en'
#     except Exception as e:
#         st.error(f"Error detecting language: {e}")
#         return 'en'

# def main():
#     st.title("InfoBot")

#     with st.sidebar:
#         st.subheader("Upload CSV Files")
#         uploaded_files = st.file_uploader("Upload CSV files", accept_multiple_files=True)
#         if uploaded_files:
#             for uploaded_file in uploaded_files:
#                 file_path = os.path.join(r"C:\Users\MYPC\OneDrive\Desktop\chatbot\chatbot_ui_lite\storage", uploaded_file.name)
#                 with open(file_path, "wb") as f:
#                     f.write(uploaded_file.getbuffer())
#             CSV_2_DB()
#             st.write(":green[DB created]")

#     user_query = st.text_input("Enter your query", key="query_input")

#     if st.button("Record Voice Query"):
#         recognizer = sr.Recognizer()
#         with sr.Microphone() as source:
#             st.write("Listening...")
#             audio = recognizer.listen(source)
#             try:
#                 user_query = recognizer.recognize_google(audio)
#                 st.write(f"Recorded Query: {user_query}")

#                 # Detect language from the voice input
#                 detected_language = detect_language(user_query)
#                 st.write(f"Detected Language: {detected_language}")

#             except sr.UnknownValueError:
#                 st.error("Sorry, I could not understand the audio.")
#                 return
#             except sr.RequestError:
#                 st.error("Sorry, there was an issue with the speech recognition service.")
#                 return
#     else:
#         detected_language = detect_language(user_query)

#     if user_query:
#         try:
#             result, query = Gen_Ai(user_query, detected_language)
#             st.write(f"SQL Query : {query}")
#             st.write(f":green[{result}]")

#             # Convert the result to speech and play it
#             play_audio(result, lang=detected_language)
#         except Exception as e:
#             st.error(f"Error: {e}")

# if __name__ == "__main__":
#     main()


# import os
# import pandas as pd
# import streamlit as st
# import whisper
# import numpy as np
# import sounddevice as sd
# import soundfile as sf
# from io import BytesIO
# from langdetect import detect, LangDetectException
# from gtts import gTTS

# # Load the Whisper model
# model = whisper.load_model("base")

# def transcribe_audio(audio_data, samplerate):
#     if samplerate != 16000:
#         audio_data = resample_poly(audio_data, 16000, samplerate)
#     audio_bytes = BytesIO()
#     sf.write(audio_bytes, audio_data, 16000, format='wav')
#     audio_bytes.seek(0)
#     result = model.transcribe(audio_bytes)
#     return result["text"]

# def detect_language(text):
#     try:
#         return detect(text)
#     except LangDetectException:
#         return 'en'
#     except Exception as e:
#         st.error(f"Error detecting language: {e}")
#         return 'en'

# def play_audio(text, lang='en'):
#     try:
#         tts = gTTS(text=text, lang=lang)
#         audio_file = "temp_audio.mp3"
#         tts.save(audio_file)
#         with open(audio_file, "rb") as f:
#             audio_bytes = f.read()
#             st.audio(audio_bytes, format='audio/mp3')
#         os.remove(audio_file)
#     except Exception as e:
#         st.error(f"Error generating audio: {e}")

# def generate_query(text):
#     # This function should generate a SQL query based on the input text
#     # Placeholder implementation, replace with actual query generation logic
#     return f"SELECT * FROM your_table WHERE your_column LIKE '%{text}%'"

# def query_database(query, df):
#     # Execute the query on the DataFrame
#     try:
#         filtered_df = df.query(query)
#         return filtered_df
#     except Exception as e:
#         st.error(f"Error querying data: {e}")
#         return pd.DataFrame()

# def main():
#     st.title("InfoBot")

#     # CSV Upload Section
#     st.sidebar.subheader("Upload CSV Files")
#     uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])
    
#     df = pd.DataFrame()
#     if uploaded_file:
#         df = pd.read_csv(uploaded_file)
#         st.sidebar.write("CSV file uploaded successfully.")
#         st.sidebar.write(df.head())  # Display the first few rows of the DataFrame for verification

#     # Voice Input Section
#     st.subheader("Voice Input")
#     if st.button("Start Live Recording"):
#         st.write("Listening...")
#         samplerate = 16000
#         duration = 5  # seconds

#         # Record audio from the microphone
#         audio_data = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1, dtype='float32')
#         sd.wait()
#         audio_data = audio_data.flatten()

#         # Transcribe the audio data
#         transcription = transcribe_audio(audio_data, samplerate)
#         st.write("Transcription:")
#         st.write(transcription)

#         # Detect language and translate if needed
#         detected_language = detect_language(transcription)
#         st.write(f"Detected Language: {detected_language}")

#         # Generate and execute query
#         query = generate_query(transcription)
#         st.write(f"Generated Query: {query}")

#         if not df.empty:
#             result_df = query_database(query, df)
#             st.write("Query Result:")
#             st.write(result_df)

#             # Convert the result to speech and play it
#             result_text = result_df.to_string(index=False)
#             play_audio(result_text, lang=detected_language)

# if __name__ == "__main__":
#     main()

#voice
# import os
# import sqlite3
# import pandas as pd
# from csv_db import CSV_2_DB
# from GenAi import Gen_Ai
# import streamlit as st
# import whisper
# import pyttsx3
# from langdetect import detect

# def play_audio(text, lang='en'):
#     engine = pyttsx3.init()
#     engine.setProperty('language', lang)  # Set language
#     audio_file = "temp_audio.wav"
#     engine.save_to_file(text, audio_file)
#     engine.runAndWait()
    
#     with open(audio_file, "rb") as f:
#         audio_bytes = f.read()
#         st.audio(audio_bytes, format='audio/wav')

# def detect_language(text):
#     try:
#         return detect(text)
#     except:
#         return 'en'

# def main():
#     st.title("InfoBot")

#     with st.sidebar:
#         st.subheader("Upload CSV Files")
#         uploaded_files = st.file_uploader("Upload CSV files", accept_multiple_files=True)
#         if uploaded_files:
#             st.write(":green[DB created]")

#     user_query = st.text_input("Enter your query", key="query_input")

#     if st.button("Record Voice Query"):
#         recognizer = whisper.load_model("base")  # Load whisper model
#         with st.audio("microphone", format="audio/wav") as source:
#             st.write("Listening...")
#             audio = source.record()
#             try:
#                 result = recognizer.transcribe(audio)
#                 user_query = result["text"]
#                 st.write(f"Recorded Query: {user_query}")

#                 # Detect language from the voice input
#                 detected_language = detect_language(user_query)
#                 st.write(f"Detected Language: {detected_language}")

#             except Exception as e:
#                 st.error(f"Error: {e}")
#                 return
#     else:
#         detected_language = detect_language(user_query)

#     if uploaded_files:
#         for uploaded_file in uploaded_files:
#             file_path = os.path.join(r"C:\Users\MYPC\OneDrive\Desktop\chatbot\chatbot_ui_lite\storage", uploaded_file.name)
#             with open(file_path, "wb") as f:
#                 f.write(uploaded_file.getbuffer())
#         CSV_2_DB()

#     if user_query:
#         try:
#             result, query = Gen_Ai(user_query, detected_language)
#             st.write(f"SQL Query : {query}")
#             st.write(f":green[{result}]")

#             # Convert the result to speech and play it
#             play_audio(result, lang=detected_language)
#         except Exception as e:
#             st.error(f"Error: {e}")

# if __name__ == "__main__":
#     main()

#voice2.0
# import streamlit as st
# import whisper
# import numpy as np
# from io import BytesIO
# from pydub import AudioSegment
# from googletrans import Translator
# from GenAi import Gen_Ai

# # Load Whisper model
# model = whisper.load_model("base")

# st.title("Voice-to-Text and SQL Query Answering")

# # Audio recording section
# st.write("Please speak your query.")

# audio_file = st.file_uploader("Upload an audio file", type=["wav", "mp3"])

# if audio_file:
#     # Convert the uploaded audio to a format Whisper can handle
#     audio_bytes = audio_file.read()
#     audio = AudioSegment.from_file(BytesIO(audio_bytes))
#     audio = audio.set_frame_rate(16000)  # Set sample rate for Whisper
#     audio = audio.set_channels(1)        # Set mono channel for Whisper
#     audio = audio.set_sample_width(2)    # Set sample width for Whisper

#     audio.export("temp.wav", format="wav")

#     # Transcribe the audio
#     result = model.transcribe("temp.wav")
#     user_query = result['text']

#     st.write("Recorded Query:", user_query)

#     # Detect language and translate
#     translator = Translator()
#     detected_lang = translator.detect(user_query).lang
#     st.write("Detected Language:", detected_lang)

#     # Process query with Gen_Ai
#     try:
#         final_answer, final_sql = Gen_Ai(user_query)
#         st.write(f"SQL Query : {final_sql}")
#         st.write(f"Answer : {final_answer}")
#     except Exception as e:
#         st.error(f"Error: {e}")

#voice 3.0
# import os
# import streamlit as st
# from pydub import AudioSegment
# import speech_recognition as sr
# from google.cloud import texttospeech
# from GenAi import Gen_Ai, translate_text

# # Initialize Google Cloud TTS client
# tts_client = texttospeech.TextToSpeechClient()

# def transcribe_audio(audio_file):
#     r = sr.Recognizer()
#     with sr.AudioFile(audio_file) as source:
#         audio = r.record(source)
#     try:
#         query = r.recognize_google(audio)
#         return query
#     except sr.UnknownValueError:
#         return "Could not understand audio"
#     except sr.RequestError as e:
#         return f"Could not request results; {e}"

# def text_to_speech(text, language_code):
#     synthesis_input = texttospeech.SynthesisInput(text=text)
#     voice = texttospeech.VoiceSelectionParams(language_code=language_code, ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL)
#     audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

#     response = tts_client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

#     with open("output.mp3", "wb") as out:
#         out.write(response.audio_content)

# st.title("Multilingual AI Chatbot")

# if st.button("Start Recording"):
#     st.write("Listening...")
#     with st.spinner("Recording..."):
#         audio_file = st.file_uploader("Upload your voice input", type=["wav"])
#         if audio_file is not None:
#             st.audio(audio_file, format="audio/wav")
#             query = transcribe_audio(audio_file)
#             st.write(f"Recorded Query: {query}")

#             detected_lang = translate_text(query, target_lang='en')
#             st.write(f"Detected Language: {detected_lang}")

#             result = Gen_Ai(query)
#             st.write("AI Response: ", result)

#             lang_code_map = {
#                 'en': 'en-US',
#                 'fr': 'fr-FR',
#                 'es': 'es-ES',
#             }
#             text_to_speech(result, lang_code_map.get(detected_lang, 'en-US'))

#             st.audio("output.mp3", format="audio/mp3")

# query_text = st.text_input("Enter your query:")
# if query_text:
#     detected_lang = translate_text(query_text, target_lang='en')
#     st.write(f"Detected Language: {detected_lang}")

#     result = Gen_Ai(query_text)
#     st.write("AI Response: ", result)

#     text_to_speech(result, lang_code_map.get(detected_lang, 'en-US'))
#     st.audio("output.mp3", format="audio/mp3")

#5th
# import streamlit as st
# import tempfile
# import os
# from GenAi import Gen_Ai, transcribe_audio, synthesize_speech  # Make sure these functions are correctly defined in GenAi.py

# # Streamlit interface
# st.title("Voice Query System")

# # Simulated or uploaded audio
# uploaded_file = st.file_uploader("Upload an audio file", type=["wav"])
# if uploaded_file is None:
#     st.warning("Please upload an audio file to proceed.")
#     st.stop()
# else:
#     # Save uploaded file
#     with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as temp_audio:
#         temp_audio.write(uploaded_file.read())
#         audio_path = temp_audio.name

#     # Transcribe audio to text
#     try:
#         text_query = transcribe_audio(audio_path)
#     except Exception as e:
#         st.error(f"Error in transcription: {e}")
#         os.remove(audio_path)
#         st.stop()
    
#     # Display transcribed text
#     st.write("Recorded Query:", text_query)
    
#     # Generate AI response
#     try:
#         response, sql_query = Gen_Ai(text_query)
#     except Exception as e:
#         st.error(f"Error in generating response: {e}")
#         os.remove(audio_path)
#         st.stop()
    
#     # Display response
#     st.write("AI Response:", response)
    
#     # Convert response to speech
#     try:
#         with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as temp_audio_output:
#             synthesize_speech(response, temp_audio_output.name)
#             audio_output_path = temp_audio_output.name
#         st.audio(audio_output_path, format='audio/mp3')
#     except Exception as e:
#         st.error(f"Error in synthesizing speech: {e}")
    
#     # Clean up temporary files
#     os.remove(audio_path)
#     os.remove(audio_output_path)



#hope
# import os
# import sqlite3
# import pandas as pd
# from csv_db import CSV_2_DB
# from GenAi import Gen_Ai
# import streamlit as st
# import speech_recognition as sr
# from gtts import gTTS
# from langdetect import detect, LangDetectException

# def play_audio(text, lang='en'):
#     try:
#         # Convert text to speech and save it to a file
#         tts = gTTS(text=text, lang=lang)
#         audio_file = "temp_audio.mp3"
#         tts.save(audio_file)
        
#         # Read the audio file and display it in Streamlit
#         with open(audio_file, "rb") as f:
#             audio_bytes = f.read()
#             st.audio(audio_bytes, format='audio/mp3')

#         # Optionally, delete the file after usage
#         os.remove(audio_file)
#     except Exception as e:
#         st.error(f"Error generating audio: {e}")

# def detect_language(text):
#     try:
#         return detect(text)
#     except LangDetectException:
#         return 'en'
#     except Exception as e:
#         st.error(f"Error detecting language: {e}")
#         return 'en'

# def main():
#     st.title("InfoBot")

#     with st.sidebar:
#         st.subheader("Upload CSV Files")
#         uploaded_files = st.file_uploader("Upload CSV files", accept_multiple_files=True)
#         if uploaded_files:
#             for uploaded_file in uploaded_files:
#                 file_path = os.path.join(r"C:\Users\MYPC\OneDrive\Desktop\chatbot\chatbot_ui_lite\storage", uploaded_file.name)
#                 with open(file_path, "wb") as f:
#                     f.write(uploaded_file.getbuffer())
#             CSV_2_DB()  # Ensure this function is defined and working
#             st.write(":green[DB created]")

#     user_query = st.text_input("Enter your query", key="query_input")

#     if st.button("Record Voice Query"):
#         recognizer = sr.Recognizer()
#         with sr.Microphone() as source:
#             st.write("Listening...")
#             audio = recognizer.listen(source)
#             try:
#                 user_query = recognizer.recognize_google(audio)
#                 st.write(f"Recorded Query: {user_query}")

#                 # Detect language from the voice input
#                 detected_language = detect_language(user_query)
#                 st.write(f"Detected Language: {detected_language}")

#             except sr.UnknownValueError:
#                 st.error("Sorry, I could not understand the audio.")
#                 return
#             except sr.RequestError:
#                 st.error("Sorry, there was an issue with the speech recognition service.")
#                 return
#     else:
#         detected_language = detect_language(user_query)

#     if user_query:
#         try:
#             result, query = Gen_Ai(user_query, detected_language)
#             st.write(f"SQL Query: {query}")
#             st.write(f":green[{result}]")

#             # Convert the result to speech and play it
#             play_audio(result, lang=detected_language)
#         except Exception as e:
#             st.error(f"Error: {e}")

# if __name__ == "__main__":
#     main()



#hope corrected tamil
import os
import sqlite3
import pandas as pd
from csv_db import CSV_2_DB
from GenAi import Gen_Ai
import streamlit as st
import speech_recognition as sr
from gtts import gTTS
from langdetect import detect, LangDetectException

def play_audio(text, lang='en'):
    try:
        # Convert text to speech and save it to a file
        tts = gTTS(text=text, lang=lang)
        audio_file = "temp_audio.mp3"
        tts.save(audio_file)
        
        # Read the audio file and display it in Streamlit
        with open(audio_file, "rb") as f:
            audio_bytes = f.read()
            st.audio(audio_bytes, format='audio/mp3')

        # Optionally, delete the file after usage
        os.remove(audio_file)
    except Exception as e:
        st.error(f"Error generating audio: {e}")

def detect_language(text):
    try:
        return detect(text)
    except LangDetectException:
        return 'en'
    except Exception as e:
        st.error(f"Error detecting language: {e}")
        return 'en'

def main():
    st.title("InfoBot")

    with st.sidebar:
        st.subheader("Upload CSV Files")
        uploaded_files = st.file_uploader("Upload CSV files", accept_multiple_files=True)
        if uploaded_files:
            for uploaded_file in uploaded_files:
                file_path = os.path.join(r"C:\Users\MYPC\OneDrive\Desktop\chatbot\chatbot_ui_lite\storage", uploaded_file.name)
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
            CSV_2_DB()  # Ensure this function is defined and working
            st.write(":green[DB created]")

    user_query = st.text_input("Enter your query", key="query_input")

    if st.button("Record Voice Query"):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            st.write("Listening...")
            audio = recognizer.listen(source)
            try:
                # Specify the language you expect the user to speak in the recognizer
                user_query = recognizer.recognize_google(audio, language="ta-IN")  # Example: Tamil
                st.write(f"Recorded Query: {user_query}")

                # If you've already specified the language, you might skip language detection
                detected_language = "ta"  # Set detected language manually to Tamil
                st.write(f"Detected Language: {detected_language}")

            except sr.UnknownValueError:
                st.error("Sorry, I could not understand the audio.")
                return
            except sr.RequestError as e:
                st.error(f"Service error: {e}")
                return
    else:
        detected_language = detect_language(user_query)

    if user_query:
        try:
            result, query = Gen_Ai(user_query, detected_language)
            st.write(f"SQL Query: {query}")
            st.write(f":green[{result}]")

            # Convert the result to speech and play it
            play_audio(result, lang=detected_language)
        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()

#hope corrected ta hi
# import os
# import sqlite3
# import pandas as pd
# from csv_db import CSV_2_DB
# from GenAi import Gen_Ai
# import streamlit as st
# import speech_recognition as sr
# from gtts import gTTS
# from langdetect import detect, LangDetectException

# def play_audio(text, lang='en'):
#     try:
#         # Convert text to speech and save it to a file
#         tts = gTTS(text=text, lang=lang)
#         audio_file = "temp_audio.mp3"
#         tts.save(audio_file)
        
#         # Read the audio file and display it in Streamlit
#         with open(audio_file, "rb") as f:
#             audio_bytes = f.read()
#             st.audio(audio_bytes, format='audio/mp3')

#         # Optionally, delete the file after usage
#         os.remove(audio_file)
#     except Exception as e:
#         st.error(f"Error generating audio: {e}")

# def detect_language(text):
#     try:
#         detected_lang = detect(text)
#         return detected_lang
#     except LangDetectException:
#         return 'en'
#     except Exception as e:
#         st.error(f"Error detecting language: {e}")
#         return 'en'

# def main():
#     st.title("InfoBot")

#     with st.sidebar:
#         st.subheader("Upload CSV Files")
#         uploaded_files = st.file_uploader("Upload CSV files", accept_multiple_files=True)
#         if uploaded_files:
#             for uploaded_file in uploaded_files:
#                 file_path = os.path.join(r"C:\Users\MYPC\OneDrive\Desktop\chatbot\chatbot_ui_lite\storage", uploaded_file.name)
#                 with open(file_path, "wb") as f:
#                     f.write(uploaded_file.getbuffer())
#             CSV_2_DB()  # Ensure this function is defined and working
#             st.write(":green[DB created]")

#     user_query = st.text_input("Enter your query", key="query_input")

#     if st.button("Record Voice Query"):
#         recognizer = sr.Recognizer()
#         with sr.Microphone() as source:
#             st.write("Listening...")
#             audio = recognizer.listen(source)
#             try:
#                 user_query = recognizer.recognize_google(audio)
#                 st.write(f"Recorded Query: {user_query}")

#                 # Detect language from the voice input
#                 detected_language = detect_language(user_query)
#                 st.write(f"Detected Language: {detected_language}")

#             except sr.UnknownValueError:
#                 st.error("Sorry, I could not understand the audio.")
#                 return
#             except sr.RequestError:
#                 st.error("Sorry, there was an issue with the speech recognition service.")
#                 return
#     else:
#         detected_language = detect_language(user_query)

#     if user_query:
#         try:
#             result, query = Gen_Ai(user_query, detected_language)
#             st.write(f"SQL Query: {query}")
#             if result:
#                 st.write(f":green[{result}]")
#                 play_audio(result, lang=detected_language)
#             else:
#                 st.warning("No SQL query was generated from the input.")
#         except Exception as e:
#             st.error(f"Error: {e}")

# if __name__ == "__main__":
#     main()



#path error
# import os
# import streamlit as st
# import wave
# import numpy as np
# from vosk import Model, KaldiRecognizer
# import speech_recognition as sr

# def transcribe_audio(file_path, model_path):
#     try:
#         model = Model(model_path)
#     except Exception as e:
#         raise RuntimeError(f"Failed to create a model: {e}")

#     rec = KaldiRecognizer(model, 16000)

#     with wave.open(file_path, "rb") as wf:
#         results = []
#         while True:
#             data = wf.readframes(4000)
#             if len(data) == 0:
#                 break
#             if rec.AcceptWaveform(data):
#                 results.append(rec.Result())

#         results.append(rec.FinalResult())
#         return ' '.join([result['text'] for result in results if 'text' in result])

# def main():
#     st.title("InfoBot")

#     with st.sidebar:
#         st.subheader("Upload CSV Files")
#         uploaded_files = st.file_uploader("Upload CSV files", accept_multiple_files=True)
#         if uploaded_files:
#             for uploaded_file in uploaded_files:
#                 file_path = os.path.join(r"C:\Users\MYPC\OneDrive\Desktop\chatbot\chatbot_ui_lite\storage", uploaded_file.name)
#                 with open(file_path, "wb") as f:
#                     f.write(uploaded_file.getbuffer())
#             st.write(":green[DB created]")

#     user_query = st.text_input("Enter your query", key="query_input")

#     if st.button("Record Voice Query"):
#         st.write("Listening...")
#         with st.spinner("Transcribing..."):
#             try:
#                 # Record and save audio
#                 audio_path = "temp.wav"
#                 recognizer = sr.Recognizer()
#                 with sr.Microphone() as source:
#                     audio = recognizer.listen(source)
#                     with open(audio_path, "wb") as f:
#                         f.write(audio.get_wav_data())

#                 # Transcribe audio
#                 model_path = "C:\Users\MYPC\OneDrive\Desktop\chatbot\chatbot_ui_lite\vosk-api-0.3.50"  # Ensure this path is correct
#                 user_query = transcribe_audio(audio_path, model_path)
#                 st.write(f"Recorded Query: {user_query}")
#                 os.remove(audio_path)

#             except Exception as e:
#                 st.error(f"Error during transcription: {e}")
#                 return

#     if user_query:
#         try:
#             # Placeholder for actual query processing
#             st.write(f"Processed Query: {user_query}")
#         except Exception as e:
#             st.error(f"Error: {e}")

# if __name__ == "__main__":
#     main()
