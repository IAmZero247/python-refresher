''' JavaScript Object Notation '''
import json

#1. Read states.json
#2. delete area code
#3. dump into a new file. newstates.json

with open('./data/states.json') as f:
  data = json.load(f)

for state in data['states']:
  del state['area_codes']

with open('./data/new_states.json', 'w') as f:
  json.dump(data, f, indent=2)