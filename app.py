from flask import Flask, request, jsonify, render_template
import google.generativeai as genai

app = Flask(_name_)

# Configure your Gemini API Key
genai.configure(api_key="AIzaSyBdNzdsdojOLRwKefQLRhZZb-Z0AjKb_KY")

# Initialize chat with DevOps-specific instructions
model = genai.GenerativeModel("models/gemini-1.5-pro")
system_prompt = (
    "You are a knowledgeable assistant that only answers DevOps-related questions like Docker, CI/CD, Kubernetes, Jenkins, Terraform, Ansible, GitHub Actions, monitoring, and cloud DevOps practices. "
    "If a question is outside DevOps, reply politely that you're only trained for DevOps topics."
)
chat = model.start_chat(history=[{"role": "user", "parts": [system_prompt]}])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.json["message"]
    try:
        response = chat.send_message(user_message)
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"reply": "Something went wrong: " + str(e)})

if _name_ == "_main_":
    app.run(debug=True)