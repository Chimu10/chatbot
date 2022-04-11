import json

with open('data.json', 'r+') as f:
    data = json.load(f)
    data['intents'][0]['patterns'][1] = 234 # <--- add `id` value.
    f.seek(0)        # <--- should reset file position to the beginning.
    json.dump(data, f, indent=4)
    f.truncate()     # remove remaining part
