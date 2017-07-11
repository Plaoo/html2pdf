import os
from flask import Flask, app, render_template, request, send_from_directory
from pdf.core import transform
import random

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def hello():
    if request.method == 'GET':
        return render_template('/index.html')
    elif request.method == 'POST':
        nome = random.randint(1000, 100000)
        nome = str(nome) + '.pdf'
        print(nome)
        html_code = {'html_code': request.form['html']}
        transform(html_code['html_code'], nome)
        return send_from_directory(directory='src', filename=nome, as_attachment=True)
    return render_template('/index.html')


if __name__ == "__main__":
    app.debug = True
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))

    app.run(host=host, port=port)
