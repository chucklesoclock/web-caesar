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
        <form id="app" method="post">
            <label>Rotate by: <input name="rot" type="number" value={rot} id="rot_input" oninput="disableDecrypt()" required></label>
            <textarea id="text_input" name="plaintext" placeholder="Enter message to encrypt here..." oninput="disableDecrypt()" required autofocus>{ciphertext}</textarea>
            <input type="submit" value="Encrypt plaintext">
            {decrypt}
        </form>
        
    <script>
    var r = document.getElementById("rot_input").value;
    var t = document.getElementById("text_input").value;
    
    function disableDecrypt() {{
        try {{
            var new_r = document.getElementById("rot_input").value;
            var new_t = document.getElementById("text_input").value;
            if (r != new_r || t != new_t) {{
                document.getElementById("decrypt").disabled = true;
            }}
            else {{
                document.getElementById("decrypt").disabled = false;
            }}
        }}
        catch (TypeError) {{
        }}
    }}
    </script>
    </body>
</html>"""


@app.route('/')
def index():
    return form.format(ciphertext='', rot=0, decrypt='')


@app.route('/', methods=['POST'])
def encrypt():
    try:
        pressed = bool(request.form['decrypt'])
    except KeyError:
        pressed = False
    text = request.form['plaintext']
    rot = int(request.form['rot'])
    if not pressed:
        cipher = caesar_encrypt(text, rot)
        button = '<button id="decrypt" name="decrypt" value=1>Undo encryption</button>\n'
    else:
        cipher = caesar_encrypt(text, abs(26-rot))
        button = ''
    return form.format(ciphertext=cipher, rot=rot, decrypt=button)


app.run(debug=True)
