from flask import Flask, request, render_template
from caesar import encrypt as caesar_encrypt
from vigenere import encrypt as vigenere_encrypt, decrypt as vigenere_decrypt

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('form.html', ciphertext='', rot=0, key='', decrypt_hide=True)


@app.route('/', methods=['POST'])
def encrypt():
    try:
        decrypt_pressed = bool(request.form['decrypt'])
    except KeyError:
        decrypt_pressed = False
    text = request.form['plaintext']
    rot = int(request.form['rot'])
    key = request.form['key']
    method = request.form['encrypt-method']
    if not decrypt_pressed:
        cipher = caesar_encrypt(text, rot) if method == 'caesar' else vigenere_encrypt(text, key)
    else:
        cipher = caesar_encrypt(text, abs(26-rot)) if method == 'caesar' \
            else vigenere_decrypt(text, key)
    return render_template('form.html', ciphertext=cipher, rot=rot, key=key,
                           decrypt_hide=decrypt_pressed, last_method=method)


app.run(debug=True)
