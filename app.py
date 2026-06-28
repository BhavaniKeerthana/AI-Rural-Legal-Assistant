from flask import Flask, render_template, request, jsonify

from database import (
    create_tables,
    save_chat,
    get_dashboard_data
)

from rag import search_answer
from translator import translate_text
from complaint_generator import generate_complaint

app = Flask(__name__)

# Create database tables
create_tables()


# ==========================
# Home Page
# ==========================
@app.route("/")
def home():
    return render_template("index.html")


# ==========================
# Ask Legal Question
# ==========================
@app.route("/ask", methods=["POST"])
def ask():

    try:

        data = request.get_json()

        question = data.get("question", "").strip()

        if not question:
            return jsonify({
                "error": "Question cannot be empty"
            }), 400

        answer, category = search_answer(question)

        save_chat(
            question,
            answer,
            category
        )

        return jsonify({
            "question": question,
            "answer": answer,
            "category": category
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# ==========================
# Translate Text
# ==========================
@app.route("/translate", methods=["POST"])
def translate():

    try:

        data = request.get_json()

        text = data.get("text", "")

        language = data.get(
            "language",
            "en"
        )

        translated = translate_text(
            text,
            language
        )

        return jsonify({
            "translated": translated
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# ==========================
# Complaint Generator
# ==========================
@app.route("/complaint", methods=["POST"])
def complaint():

    try:

        data = request.get_json()

        name = data.get("name", "")

        issue = data.get("issue", "")

        complaint_text = generate_complaint(
            name,
            issue
        )

        return jsonify({
            "complaint": complaint_text
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# ==========================
# Admin Dashboard
# ==========================
@app.route("/admin")
def admin():

    try:

        (
            total_queries,
            property_count,
            consumer_count,
            cybercrime_count,
            government_count,
            chats
        ) = get_dashboard_data()

        return render_template(
            "admin.html",
            total_queries=total_queries,
            property_count=property_count,
            consumer_count=consumer_count,
            cybercrime_count=cybercrime_count,
            government_count=government_count,
            chats=chats
        )

    except Exception as e:

        return f"Dashboard Error: {str(e)}"


# ==========================
# Health Check
# ==========================
@app.route("/health")
def health():

    return jsonify({
        "status": "running"
    })


# ==========================
# Run Application
# ==========================
if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )