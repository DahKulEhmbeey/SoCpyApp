import json
from flask import Flask, render_template, request

app = Flask(__name__)

CONTACTS_DICT = {}


def add_contact(name, number):
  global CONTACTS_DICT
  # 1. Add a new contact to the CONTACTS_DICT.
  # 2. Deduce a way to check if the operation was successful
  #    and return either True or False indicating the operation error status.
  #    Return True if there is an error, and False if there is no error.

  CONTACTS_DICT[name] = number

  error_status = False
  if CONTACTS_DICT[name] != number:
    error_status = True

  return error_status


def edit_contact():
  global CONTACTS_DICT
  # Edit a particular contact and return either True
  # or False indicating the operation status
  status = False # False by default, return the appropriate boolean
  return status


def search_for_contact(name):
  global CONTACTS_DICT
  # Search for a particular contact and return either True
  # or False indicating the operation status

  names_list = list(CONTACTS_DICT.keys())
  numbers_list = list(CONTACTS_DICT.values())

  matched_contacts = []
  for key in names_list:
    if name.lower() in key.lower():
      matched_contacts.append({'name': key, 'number': CONTACTS_DICT[key]})
  
  number = name
  for key in numbers_list:
    if number in key:
      matched_contacts.append({'name': names_list[numbers_list.index(key)], 'number': key})

  return matched_contacts


@app.route('/')
def index():
  return render_template('add-contact.html')


@app.route('/contacts')
def contacts():
  # flat_contacts = [{'name': key, 'number': CONTACTS_DICT[key]} for key in CONTACTS_DICT.keys()]
  flat_contacts = []
  for key in CONTACTS_DICT.keys():
    flat_contacts.append({
      'name': key,
      'number': CONTACTS_DICT[key]
    })
  
  data = {'heading': 'All', 'length': len(flat_contacts), 'payload': flat_contacts}
  return render_template('all-contacts.html', data=data)


@app.route('/add-contact', methods=['POST'])
def save_contact():
  name = request.json['name']
  number = request.json['number']
  op_error_status = add_contact(name, number)
  return json.dumps({'error': op_error_status})


@app.route('/search')
def search():
  name = request.args['name']
  the_contact = search_for_contact(name)
  data = {'heading': 'Searched', 'length': len(the_contact), 'payload': the_contact}
  return render_template('all-contacts.html', data=data)


if __name__ == "__main__":
  app.run(debug=True, port=3001, host='0.0.0.0')

