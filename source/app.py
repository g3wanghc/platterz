import os
import requests

from flask import Flask, jsonify
from flask import request, url_for

from helpers import *

app = Flask(__name__)

cache = {}

@app.route('/api', methods=['POST'])
def api():
    action_1 = [
        make_action('food', 'apple'),
        make_action('food', 'oranges'),
        make_action('food', 'bananas'),
    ]

    action_2 = [
        make_action('colour', 'red'),
        make_action('colour', 'yellow'),
        make_action('colour', 'blue'),
    ]

    action_3 = [
        make_action('spicyness', 'extreme'),
        make_action('spicyness', 'hot'),
        make_action('spicyness', 'mild'),
    ]

    attach_1 = make_attachment('Choose a food: ', 'callback_id_food', action_1)
    attach_2 = make_attachment('Choose a colour: ', 'callback_id_colour', action_2)
    attach_3 = make_attachment('Choose a spicyness: ', 'callback_id_spicyness', action_3)

    attachments = [attach_1, attach_2, attach_3]

    r = make_response('Dietary Prefrences: ', attachments)
    return jsonify(r)

@app.route('/interaction', methods=['POST'])
def callback():
    content = dict(request.form)['payload']

    user = content['user']['id'];
    print("got request 2")
    value = 0

    if user in cache:
        name = content['actions']['name']
        value = content['actions']['value']
        cache[user][name] = value

        value += 1
    else:
        cache[user] = {}

    action_1 = [
        make_action('food', 'apple'),
        make_action('food', 'oranges'),
        make_action('food', 'bananas'),
    ]

    action_2 = [
        make_action('colour', 'red'),
        make_action('colour', 'yellow'),
        make_action('colour', 'blue'),
    ]

    action_3 = [
        make_action('spicyness', 'extreme'),
        make_action('spicyness', 'hot'),
        make_action('spicyness', 'mild'),
    ]

    meta_data = {
        "title": "Testing clicks",
        "fields": [
            {
                "title": "Volume",
                "value": value,
            }
        ]
    }

    attach_1 = make_attachment('Choose a food: ', 'callback_id_food', action_1)
    attach_2 = make_attachment('Choose a colour: ', 'callback_id_colour', action_2)
    attach_3 = make_attachment('Choose a spicyness: ', 'callback_id_spicyness', action_3)

    attachments = [meta_data, attach_1, attach_2, attach_3]

    r = make_response('Dietary Prefrences: ', attachments)
    return jsonify(r)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
