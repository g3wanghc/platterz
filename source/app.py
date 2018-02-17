from flask import Flask
from helpers import *

app = Flask(__name__)

@app.route('/')
def hello_world():

    action_1 = {
        make_action('food', 'apple'),
        make_action('food', 'oranges'),
        make_action('food', 'bananas'),
    }

    action_2 = {
        make_action('colour', 'red'),
        make_action('colour', 'yellow'),
        make_action('colour', 'blue'),
    }

    action_3 = {
        make_action('spicyness', 'extreme'),
        make_action('spicyness', 'hot'),
        make_action('spicyness', 'mild'),
    }

    actions = [action_1, action_2, action_3]

    attach_1 = make_attachment('Choose an option: ', 'callback_id_001', actions)

    attachments = [attach_1]

    r = make_response('Hello, World!', attachments)

    return json.dumps(r).replace("\'", "\"")