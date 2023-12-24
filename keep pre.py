from flask import Flask, render_template, request
from colorama import Fore
import google.generativeai as genai

app = Flask(__name__)

# Configure GPT-3 API
genai.configure(api_key="AIzaSyDMtg6xEuqUNi_25i9chFjv21tqb2YM4s4")

# Set up the model
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
]

model = genai.GenerativeModel(
    model_name="gemini-pro",
    generation_config=generation_config,
    safety_settings=safety_settings,
)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/pdf")
def pdf():
    return render_template("pdf.html")


@app.route("/process", methods=["POST"])
def process():
    prompt = request.form["prompt"]
    response = model.generate_content(prompt)
    return {"response": response.text}

if __name__ == "__main__":
    app.run(debug=True)