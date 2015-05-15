import json

from flask import Flask
from flask import request
from flask import render_template
import addressbook_pb2
import data

app = Flask(__name__)

# Content-type:  application/x-protobuf

# class GLOBAL:
#     book_pb = addressbook_pb2.AddressBook(
#         contacts=[
#             addressbook_pb2.Contact(
#                 address=addressbook_pb2.Address(
#                     first_name='Alice',
#                     last_name='Bertram',
#                 ),
#                 phone_numbers=[
#                     addressbook_pb2.Phone(type=addressbook_pb2.MOBILE, number='123'),
#                     addressbook_pb2.Phone(type=addressbook_pb2.LANDLINE, number='567'),
#                 ],
#             )
#         ],
#     )
#     book_dict = {
#         'contacts': [
#             {
#                 'address': {
#                     'first_name': 'Alice',
#                     'last_name': 'Bertram',
#                 },
#                 'phone_numbers': [
#                     {'type': 'MOBILE', 'number': '123'},
#                     {'type': 'LANDLINE', 'number': '567'},
#                 ]
#             },
#         ],
#     }


# @app.route('/api/full.json', methods=['GET', 'POST'])
# def json_full():
#     if flask.request.method == 'POST':
#         GLOBAL.book_dict = json.loads(flask.request.data)
#     elif flask.request.method == 'GET':
#         return json.dumps(GLOBAL.book_dict)


# @app.route('/api/full.pb', methods=['GET', 'POST'])
# def pb_full():
#     if flask.request.method == 'POST':
#         GLOBAL.book_pb.ParseFromString(flask.request.data)
#     elif flask.request.method == 'GET':
#         return GLOBAL.book_pb.SerializeToString()


# @app.route('/api/search-by-name.json', methods=['GET'])
# def json_search_by_name():
#     name = flask.request.args.get('name')
#     result = []

#     for x in GLOBAL.book_dict.get('contacts', []):
#         if name in x['address']['first_name'] or name in x['address']['last_name']:
#             result.append(x)

#     return json.dumps(result)


# @app.route('/api/search-by-name.pb', methods=['GET'])
# def pb_search_by_name():
#     name = flask.request.args.get('name')
#     result = addressbook_pb2.SearchResult()

#     for x in GLOBAL.book_pb.contacts:
#         if name in x.address.first_name or name in x.address.last_name:
#             result.contacts.extend([x])

#     return result.SerializeToString()


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/api/contacts', methods=['GET', 'POST'])
def contacts():
    wants_json = request.headers['Accept'] == "application/json"
    if request.method == 'GET':
        if wants_json:
            return json.dumps(data.contacts)
        return data.get_protobuf_data().SerializeToString()



if __name__ == '__main__':
    app.run(debug=True)
