# web-caesar
Flask implementation of simple encryption algorithms in a Flask web application. 

Allows you to input and encrypt messages using the caesar and vigenere ciphers. 

If you accidentally encrypt the wrong message, you can quickly undo the encryption. This button is disabled as soon as the decrypted message is changed in the textbox, and is provided as an exercise in early JavaScript. 

Features include input validation and some toggling. 

## To Run

- Clone or download the repository
- Have [Python](https://www.python.org/downloads/) installed on your machine
- Download [Flask](http://flask.pocoo.org/)
- Start a local Flask web server
  - In a terminal or command prompt, navigate to the downloaded folder and run `python main.py`. (The flask docs have an alternate way of doing this.) 
  - In a browser, go to the URL indicated by `Running on http://XXX.X.X.X:YYYY/` 
- Enjoy

## Future Enhancements

- add decryption capability with inputed shift for caesar or key for vingenere ciphers. 
