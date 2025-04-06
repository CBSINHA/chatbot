from flask import Flask, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-1.5-pro")

# Create Flask app
app = Flask(_name_)

# Custom system prompt (adjust as needed)
SYSTEM_PROMPT = (
    "You are a helpful assistant that only answers questions related to DevOps. "
    "If the question is unrelated to DevOps (like food, travel, games, etc.), respond with: "
    "'Sorry, I can only help with DevOps-related queries.'"
)

# Define chatbot route
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")

    if not user_input:
        return jsonify({"error": "Message is required"}), 400

    try:
        response = model.generate_content([SYSTEM_PROMPT, user_input])
        reply = response.text.strip()
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Home route (optional)
@app.route("/", methods=["GET"])
def home():
    return "DevOps Chatbot is running! 🚀"

if _name_ == "_main_":
    app.run(debug=True)