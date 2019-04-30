import json
from flask import Flask, render_template, request
from src.edit import edit_contact
from src.save import add_contact
from src.search import search_for_contact


app = Flask(__name__)

@app.route('/')
def index():
  return render_template('add-contact.html')


@app.route('/contacts')
def contacts():
  return 'Contacts here'


@app.route('/add-contact', methods=['POST'])
def save_contact():
  name = request.json['name']
  number = request.json['number']
  op_status = add_contact(name, number)
  return json.dumps({'error': op_status})


if __name__ == "__main__":
  app.run(debug=True, port=3001)
