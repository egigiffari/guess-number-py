from flask import Flask, render_template, request
import random

app = Flask(__name__)
low_num = 1
high_num = 100
secret_num = random.randint(low_num, high_num)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html.j2')
    
    elif request.method == 'POST':
        guess = request.form.get('number')
        global secret_num

        if not guess.isdigit():
            return render_template('index.html.j2')

        guess = int(guess)
        status = ""

        if guess < secret_num:
            status = "Too Low, Try Again"
        elif guess > secret_num:
            status = 'Too High, Try Again'
        else:
            status = f"Correct!, the number is {secret_num}"
            secret_num = random.randint(low_num, high_num)

        return render_template('index.html.j2', status=status)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5000", debug=True)