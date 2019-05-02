import json
from flask import Flask, render_template, request

app = Flask(__name__)

CONTACTS_LIST = []


def add_contact(name, number):
  global CONTACTS_LIST
  # 1. Add a new contact to the CONTACTS_LIST.
  # 2. Deduce a way to check if the operation was successful
  #    and return either True or False indicating the operation status.
  #    Return True if there is an error, and False if there is no error.
  error_status = False # False by default, return the appropriate boolean
  return error_status


def edit_contact():
  global CONTACTS_LIST
  # Edit a particular contact and return either True
  # or False indication the operation status
  status = False # False by default, return the appropriate boolean
  return status


def search_for_contact():
  global CONTACTS_LIST
  # Search for a particular contact and return either True
  # or False indication the operation status
  status = False # False by default, return the appropriate boolean
  return status


@app.route('/')
def index():
  return render_template('add-contact.html')


@app.route('/contacts')
def contacts():
  return json.dumps(CONTACTS_LIST)


@app.route('/add-contact', methods=['POST'])
def save_contact():
  name = request.json['name']
  number = request.json['number']
  op_error_status = add_contact(name, number)
  return json.dumps({'error': op_error_status})


if __name__ == "__main__":
  app.run(debug=True, port=3001, host='0.0.0.0')

