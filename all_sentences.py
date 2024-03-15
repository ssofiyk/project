from flask import Flask, render_template, request

app = Flask(__name__)

sentence = "Бабушка любит чай"

@app.route('/', methods=['GET', 'POST'])
def home():
    global correct_answers
    if request.method == 'POST':
        user_sentence = request.form.get('sentence')
        if user_sentence == sentence:
            result = "Вы правильно записали предложение!"
            correct_answers += 1
        else:
            result = "Вы неправильно записали предложение."
        return render_template('result_all_sentences.html', result=result)
    else:
        return render_template('index_all_sentences.html', sentence=sentence)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

