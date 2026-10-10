from flask import Flask, request, jsonify
import os

app = Flask(name)

@app.route("/")
def home():
    return "AsifBhai AI backend is running!"

@app.route("/health")
def health():
return jsonify({
"status": "ok",
"app": "AsifBhai AI"
})

@app.route("/chat", methods=["POST"])
def chat():
data = request.get_json(silent=True) or {}
message = data.get("message", "").strip()

if not message:
    return jsonify({"error": "Message is required"}), 400

return jsonify({
    "reply": "Bhai, tumhara message mil gaya: " + message
})

if name == "main":
app.run(
host="0.0.0.0",
port=int(os.environ.get("PORT", 8080))
)
