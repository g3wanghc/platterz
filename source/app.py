import os
import requests
import json
import sets

from flask import Flask, jsonify
from flask import request, url_for

from helpers import *

app = Flask(__name__)

cache = {
    "is_active": True,
    "in_channel": False,
    "is_admin": True,
    "admin": {},
    "users": {
        "in": set(),
        "out": set(),
    },
    "restaurant": {},
    "restaurant_list": [
        {
            "id": 84,
            "restaurant_id": "120",
            "name": "California Sandwiches",
            "name_slug": "california-sandwiches",
            "slug": "downtown-435-yonge-st"
        },
        {
            "id": 190,
            "restaurant_id": "205",
            "name": "Presse Cafe",
            "name_slug": "presse-cafe",
            "slug": "bloor-st-85-bloor-st-e"
        },
        {
            "id": 102,
            "restaurant_id": "68",
            "name": "Craft Kitchen",
            "name_slug": "craft-kitchen",
            "slug": "bloor-st-85-st-e"
        },
    ]
}

@app.route('/api', methods=['POST'])
def api():
    # action_1 = [
    #     make_action('food', 'apple'),
    #     make_action('food', 'oranges'),
    #     make_action('food', 'bananas'),
    # ]

    # action_2 = [
    #     make_action('colour', 'red'),
    #     make_action('colour', 'yellow'),
    #     make_action('colour', 'blue'),
    # ]

    action = [
        make_action('restaurant', restaurant['name'])
        for restaurant in cache['restaurant_list']
    ]

    attach_1 = make_attachment('Choose a place: ', 'callback_id_food', action)
    # attach_2 = make_attachment('Choose a colour: ', 'callback_id_colour', action_2)
    # attach_3 = make_attachment('Choose a spicyness: ', 'callback_id_spicyness', action_3)

    attachments = [attach_1]

    r = make_response('Choose a restaurant', attachments)
    return jsonify(r)

@app.route('/interaction', methods=['POST'])
def callback():
    print('in callback')
    content = json.loads(dict(request.form)['payload'][0])
    print(content)

    user = content['user']['id']
    print('user ', user)

    if user in cache:
        name = content['actions'][0]['name']
        value = content['actions'][0]['value']
        cache[user][name] = value
    else:
        cache[user] = {}
        print('user cached')

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
                "title": "Attending",
                "value": len(cache["users"]["in"]),
            }
        ]
    }

    attach_1 = make_attachment('Choose a food: ', 'callback_id_food', action_1)
    attach_2 = make_attachment('Choose a colour: ', 'callback_id_colour', action_2)
    attach_3 = make_attachment('Choose a spicyness: ', 'callback_id_spicyness', action_3)

    attachments = [meta_data, attach_1, attach_2, attach_3]
    print('created attatchement')

    r = make_response('Dietary Prefrences: ', attachments, in_channel=True)
    print('created response')

    return jsonify(r)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
