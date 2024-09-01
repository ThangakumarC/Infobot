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
            CSV_2_DB()
            st.write(":green[DB created]")

    user_query = st.text_input("Enter your query", key="query_input")

    if st.button("Record Voice Query"):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            st.write("Listening...")
            audio = recognizer.listen(source)
            try:
                user_query = recognizer.recognize_google(audio)
                st.write(f"Recorded Query: {user_query}")

                # Detect language from the voice input
                detected_language = detect_language(user_query)
                st.write(f"Detected Language: {detected_language}")

            except sr.UnknownValueError:
                st.error("Sorry, I could not understand the audio.")
                return
            except sr.RequestError:
                st.error("Sorry, there was an issue with the speech recognition service.")
                return
    else:
        detected_language = detect_language(user_query)

    if user_query:
        try:
            result, query = Gen_Ai(user_query, detected_language)
            st.write(f"SQL Query : {query}")
            st.write(f":green[{result}]")

            # Convert the result to speech and play it
            play_audio(result, lang=detected_language)
        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()


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
