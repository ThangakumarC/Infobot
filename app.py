# flask+LLama
from flask import Flask, request, render_template, jsonify, session
from csv_db import CSV_2_DB
from GenAi import Gen_Ai
import os

app = Flask(__name__)
app.secret_key = 'secret'  # Needed for session
UPLOAD_FOLDER = os.path.join(os.getcwd(), "storage")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    session['history'] = []  # Clear session on fresh visit
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files.get('file')
    if not file:
        return jsonify({'error': 'No file uploaded'}), 400

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    try:
        CSV_2_DB()  # Use your existing method
        return jsonify({'message': 'CSV uploaded and database updated'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    question = data.get('question', '').strip()
    if not question:
        return jsonify({'error': 'No question provided'}), 400

    try:
        answer, _ = Gen_Ai(question)
        session['history'].append({'user': question, 'bot': answer})
        return jsonify({'answer': answer, 'history': session['history']})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
