
from flask import Flask, request, jsonify
import openai
import os
from flask_cors import CORS

# API-Key sicher speichern (hier direkt eingetragen oder über Umgebungsvariable)
openai.api_key = os.getenv("OPENAI_API_KEY", "sk-DEIN_API_KEY_HIER")

app = Flask(__name__)
CORS(app)  # CORS erlaubt Zugriff von deiner Web-App

@app.route("/gpt", methods=["POST"])
def gpt():
    data = request.json
    prompt = data.get("prompt", "")
    if not prompt:
        return jsonify({"error": "Kein Prompt erhalten"}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        answer = response.choices[0].message.content
        return jsonify({"response": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
