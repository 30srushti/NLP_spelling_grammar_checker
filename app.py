from flask import Flask, render_template, request
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

app = Flask(__name__)

tokenizer = AutoTokenizer.from_pretrained("vennify/t5-base-grammar-correction")
model = AutoModelForSeq2SeqLM.from_pretrained("vennify/t5-base-grammar-correction")

def correct_grammar(text):
    inputs = tokenizer.encode(text, return_tensors="pt", max_length=512, truncation=True)
    outputs = model.generate(inputs, max_length=512, num_beams=4, early_stopping=True)
    corrected = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return corrected

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", corrected_text="")

@app.route("/spell", methods=["POST"])
def spell_checker():
    user_text = request.form.get("text", "")
    corrected_text = correct_grammar(user_text)
    return render_template("index.html", corrected_text=corrected_text)

if __name__ == "__main__":
    app.run(debug=True)