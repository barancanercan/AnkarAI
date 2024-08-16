
from flask import Flask, jsonify, render_template, request

from ankarai import chain

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    question = request.form.get("question")
    response = chain.invoke({"question": question})

    if isinstance(response, dict):
        answer = response.get("text", "Bir hata oluştu, lütfen tekrar deneyin.")
    else:
        answer = "Bir hata oluştu, lütfen tekrar deneyin."

    # Cevabın sonuna teşekkür mesajı ekliyoruz
    answer += "\n\nAnkarAI kullandığınız için teşekkür ederim."

    return jsonify({"answer": answer})


if __name__ == "__main__":
    app.run(debug=True)
