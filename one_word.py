from flask import Flask, render_template, request

app = Flask(__name__)

sentence = "Бабушка любит чай"
missing_word = "______"

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_word = request.form.get('word')
        if user_word.lower() == sentence.split()[0].lower():
            result = "Вы правильно вписали слово!"
        else:
            result = "Вы неправильно вписали слово."
        return render_template('result_one_word.html', result=result)
    else:
        return render_template('index_one_word.html', sentence=sentence, missing_word=missing_word)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
