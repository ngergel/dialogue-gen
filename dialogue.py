from random import randint

templates = [
	'INTENT| to |MEET| with |AUTHORITY|?',
	'INTENT| to |MEET| with |AUTHORITY|, huh?',
	'PEOPLE| at McCarran |APPRECIATION| what you\'ve done.',
	'You |SHOULD| |CONSIDER| enlisting, we could use the |HELP|.'
]

synonyms = {
	'INTENT': ['intend', 'here', 'are you here', 'you here', 'checking in'],
	'MEET': ['meet', 'talk'],
	'AUTHORITY': ['the boss', 'the brass', 'admin'],
	'PEOPLE': ['lots of folks', 'people here', 'everyone here', 'all of us'],
	'APPRECIATION': ['really appreciate', 'are thankful for', 'appreciate', 'couldn\'t be more thankful for'],
	'SHOULD': ['oughtta', 'should', 'really should'],
	'CONSIDER': ['consider', 'think about'],
	'HELP': ['help', 'extra set of hands']
}


def dialogue():
	global templates, synonyms

	msg = templates[randint(0, len(templates) - 1)]
	punctuation, msg = msg[-1], msg[:len(msg) - 1].split('|')

	for i in range(len(msg)):
		if msg[i] in synonyms:
			msg[i] = synonyms[msg[i]][randint(0, len(synonyms[msg[i]]) - 1)]

	msg = ''.join(msg) + punctuation
	msg = msg[0].upper() + msg[1:]

	print(msg)

def main():
	dialogue()












if __name__ == '__main__':
	main()