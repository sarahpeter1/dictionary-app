# dictionary system in python 

import requests 

#  function to fetch word meaning from an api
def get_word_meaning(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        meanings = data[0]['meanings']
        
        print(f"Word: {word}")
        for meaning in meanings:
            part_of_speech = meaning['partOfSpeech']
            print(f"Part of Speech: {part_of_speech}")
            for definition in meaning['definitions']:
                print(f"- Definition: {definition['definition']}")
                if 'example' in definition:
                    print(f"  Example: {definition['example']}")
    else:
        print("Word not found. Please try another word.")


    word = input("Enter a word: ")
    get_word_meaning(word)
