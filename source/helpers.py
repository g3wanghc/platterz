import json

BASE_CATERING_URL = 'https://www.platterz.ca/toronto/catering'
BASE_API_URL = '' # just in case :)

def make_action(name, text):
	button = {
		'name': name,
		'text': text,
		'type': 'button',
		'value': text
	}
	return button

def make_attachment(attachement_prompt, callback_id, actions_arr):
	actions = []
	for action in actions_arr:
		actions.append(action)

	attachment = {
		'text': attachement_prompt,
		'callback_id': callback_id,
		'actions': actions,
		'value': 'bananas'
	}
	return attachment

def make_response(prompt_question, attachments_arr, in_channel=False):
	attachments = []
	for attachment in attachments_arr:
		attachments.append(attachment)

	response = {
                'response_type': 'in_channel' if in_channel else 'ephemeral',
		'text': prompt_question,
		'attachments': attachments
	}

	return response

def restuarant_url(restaurant):
    return str.format('{}/{}-{}/{}-{}',
                      BASE_CATERING_URL,
                      restaurant['restaurnt_id'],
                      restaurant['name_slug'],
                      restaurant['id'],
                      restaurant['slug'])
