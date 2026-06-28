# ⚖️ AI Rural Legal Assistant

## 📖 Overview

AI Rural Legal Assistant is a web-based application developed using Python Flask to provide basic legal guidance to users. It helps users understand common legal issues related to property disputes, consumer complaints, cybercrime, and government services through an interactive chatbot.

The application also supports multilingual translation, complaint letter generation, voice interaction, chat history storage, and an admin dashboard for monitoring user queries.

---

## ✨ Features

- 💬 Legal FAQ-based chatbot
- 🏠 Property dispute guidance
- 🛒 Consumer complaint assistance
- 🔒 Cybercrime reporting guidance
- 🏛️ Government service information
- 🌐 Multilingual translation
- 🎤 Voice input (Speech Recognition)
- 🔊 Voice output (Text-to-Speech)
- 📝 Automatic complaint letter generation
- 💾 SQLite database for chat history
- 📊 Admin dashboard with query statistics
- 📱 Responsive and user-friendly interface

---

## 🛠️ Technologies Used

### Backend
- Python
- Flask
- SQLite

### Frontend
- HTML
- CSS
- JavaScript

### Libraries
- Pandas
- Flask
- Deep Translator / Google Translate
- Speech Recognition
- pyttsx3

---

## 📂 Project Structure

```
AI_Rural_Legal_Assistant/
│
├── app.py
├── database.py
├── rag.py
├── translator.py
├── complaint_generator.py
├── speech.py
├── legal_assistant_dataset.csv
│
├── database/
│   └── legal.db
│
├── templates/
│   ├── index.html
│   └── admin.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── README.md
```

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/AI-Rural-Legal-Assistant.git
```

### Navigate to the project

```bash
cd AI-Rural-Legal-Assistant
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 🎯 Modules

### Legal Assistant
Answers user questions related to:
- Property disputes
- Consumer complaints
- Cybercrime
- Government services

### Translation
Translates legal information into multiple languages.

### Complaint Generator
Generates complaint letters based on user input.

### Voice Assistant
Supports voice-based interaction using Speech Recognition and Text-to-Speech.

### Admin Dashboard
Displays:
- Total queries
- Category-wise statistics
- Recent chat history

---

## 📌 Future Enhancements

- Integration with Llama 3, Gemma, or Mistral
- Retrieval-Augmented Generation (RAG)
- PDF legal document upload and analysis
- OCR for scanned legal documents
- User authentication and authorization
- Dashboard analytics with charts
- Integration with official government legal resources

---

## 👩‍💻 Author

**Bhavani Keerthana**

B.Tech – Artificial Intelligence and Data Science

Velammal Engineering College

---
