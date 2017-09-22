from flask import Flask, request
from caesar import encrypt as caesar_encrypt

app = Flask(__name__)

form = """<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
            #rot_input {{
                width: 3em;
                border-radius: 0px;
            }}
            #rot_input:invalid {{
                border-right: 2px solid;
                border-color: red;
            }}
        </style>
    </head>
    <body>
        <form method="post">
            <label>Rotate by: <input name="rot" type="number" value={rot} id="rot_input" required></label>
            <textarea name="plaintext" placeholder="Enter message to encrypt here..." required autofocus>{ciphertext}</textarea>
            <input type="submit" value="Encrypt plaintext">
        </form>
    </body>
</html>"""


@app.route('/')
def index():
    return form.format(ciphertext='', rot=0)


@app.route('/', methods=['POST'])
def encrypt():
    text = request.form['plaintext']
    rot = int(request.form['rot'])
    return form.format(ciphertext=caesar_encrypt(text, rot), rot=rot)

app.run(debug=True)
