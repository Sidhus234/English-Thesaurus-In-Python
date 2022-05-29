import json
from difflib import get_close_matches

data = json.load(open(".//Data//data.json", "r"))


def translate(word):
    if word in data.keys():
        return data[word]

    # Check for nouns
    elif word.title() in data.keys():
        return data[word.title()]

    # Check for acronyms
    elif word.upper() in data.keys():
        return data[word.upper()]

    # Find similar words
    elif len(get_close_matches(word, data.keys(), n=1)) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes or N if no." %
                   get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys(), n=1)[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your query."
    else:
        return "The word doesn't exist. Please double check it."


word = input("Enter word: ").lower()
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
