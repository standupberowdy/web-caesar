from flask import Flask, request 
from caesar import rotate_string 

"""
This is our web application! It's built using a 'framework' (a bunch of tools) called Flask http://flask.pocoo.org/

#import some modules from flask
from flask import Flask, render_template, request, url_for
#import some 2 functions from helpers.py
from caesar import sanitise_text_input, sanitise_number_input

#Instantiate (create) our flask app object
app = Flask(__name__)
#debug mode so our browser doesn't cache (save) our page
app.debug = True

#our index (main) page
@app.route('/')
def index():
    return render_template('index.html')

#encyption page
@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    #if the user is requesting the page via GET request, just return our webpage in html
    if request.method == 'GET':
        return render_template('encrypt.html')
    #if the user POSTs us some data, let's encrypt it and return the encrypted message
    elif request.method == 'POST':
        message = sanitise_text_input(request.form["message"])
        key = sanitise_number_input(request.form['key'])
        encryptedmessage = encrypt_caesar(message, key)
        return render_template('encrypt.html', encrypted_message=encryptedmessage)

#decryption page
@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():
    return render_template('decrypt.html')


#function to encrypt users message using key provided
def encrypt_caesar(message, key):
    #TODO
    return 0

#function to decrypt a message
def decrypt_caesar(message):
    #TODO
	return 0

"""
app = Flask(__name__)
app.config['DEBUG'] = True
form = """
<!DOCTYPE html>

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
        </style>
    </head>

    <body>
      <form method="POST">
      <div>
	      <label for="rot"> Rotate by:</label>
	      <input name="rot" type="text" value="0">
	      <p class="error"></p>
	  </div>    
      <textarea type="text" name="text">{0}</textarea>
      <h1 name="cypher"></h1>
      <br>
      <input type="Submit">
      </form>
    </body>
</html>
"""
@app.route("/")
def index():
	return form
@app.route("/", methods=['POST'])
def encrypt():
	r = int(request.form["rot"])
	t = request.form["text"]
	cypher = rotate_string(t,r)
	return form.format(cypher)
app.run()
