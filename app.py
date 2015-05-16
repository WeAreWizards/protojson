import json

from flask import Flask
from flask.ext.compress import Compress
from flask import request
from flask import render_template
import addressbook_pb2
import data

app = Flask(__name__)
Compress(app)

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
