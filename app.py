import json

from flask import Flask
from flask.ext.compress import Compress
from flask import request
from flask import render_template
import addressbook_pb2
import data

app = Flask(__name__)
Compress(app)


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

    # POST branch
    if wants_json:
        data.contacts.append(request.get_json())
        return json.dumps(data.contacts)

    # Won't persist protobuf ones, just to see how that works
    #import ipdb; ipdb.set_trace()
    # address_book = data.get_protobuf_data()
    # address_book.append(
    #     addressbook_pb2.Contact(request.get_json()
    #     )
    # )
    return data.get_protobuf_data().SerializeToString()

if __name__ == '__main__':
    app.run(debug=True)
