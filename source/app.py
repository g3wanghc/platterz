from flask import Flask
from helpers import *

app = Flask(__name__)

@app.route('/')
def hello_world():

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

    r = make_response('Dietary preferences: ', attachments)

    return json.dumps(r).replace("\'", "\"")
