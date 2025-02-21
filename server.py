import os

import openai
from dotenv import load_dotenv
from flask import Flask, render_template, request

load_dotenv()  # load env vars from .env file
#openai.api_key = os.getenv("OPENAI_API_KEY") 키바꾸기!!!!!!!
openai.api_key = os.getenv("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")

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get_response")
def get_response():
    message = request.args.get("message")
    completion = openai.ChatCompletion.create(
        # You can switch this to `gpt-4` if you have access to that model.
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}],
    )
    response = completion["choices"][0]["message"]["content"]
    return response


if __name__ == "__main__": 
    #포트수정해줫음
    app.run(debug=True,host='0.0.0.0',port=9090)
