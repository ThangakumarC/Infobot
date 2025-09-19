# 📊 InfoBot – AI Chatbot for CSV Data Queries

**InfoBot** is a smart and multilingual AI chatbot that allows users to upload CSV files and ask natural language questions about their data — even in regional languages like Tamil, Hindi, etc. The system translates the query, generates an SQL command, executes it on the dataset, and returns a friendly, human-like response.

---

## ⚙️ Built With

- 🧠 **Groq's LLaMA 3–70B** via LangChain  
- 🌐 **Flask** (Python micro web framework)  
- 📄 **SQLite** (auto-generated from uploaded CSVs)  
- 🎨 **Tailwind CSS** (UI framework)  

---

## 🚀 Features

- 🧠 LLM-powered intelligence via **LLaMA 3**  
- 📁 Upload and query CSV files dynamically  
- 🗣️ Supports **natural language queries in any language**  
- 🧾 Generates and executes SQL commands internally  
- 🖼️ Clean, modern UI using Tailwind CSS  
- 🔒 Local **SQLite3 database** for secure storage  

---

## 🗂️ Project Structure

chatbot/
├── app.py                
├── GenAi.py              
├── csv_db.py             
├── templates/
│   └── index.html        
├── storage/
│   └── DataBase.db       

---
