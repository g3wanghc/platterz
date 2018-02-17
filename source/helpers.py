import json

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

def make_response(prompt_question, attachments_arr):
	attachments = []
	for attachment in attachments_arr:
		attachments.append(attachment)

	response = {
		'text': prompt_question,
		'attachments': attachments
	}

	return response
