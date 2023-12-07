import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer
from flask import Flask, render_template, request

app = Flask(__name__)

model_name = "t5-small"
model = T5ForConditionalGeneration.from_pretrained(model_name)
tokenizer = T5Tokenizer.from_pretrained(model_name)

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = None
    if request.method == 'POST':
        article = request.form['article']  # Assuming input named 'article' from a form
        
        inputs = tokenizer.encode("summarize: " + article, return_tensors="pt", max_length=512, truncation=True)
        summary_ids = model.generate(inputs, max_length=150, min_length=30, length_penalty=2.0, num_beams=4, early_stopping=True)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        
    return render_template('index.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
