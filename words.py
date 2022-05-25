import requests

url = 'https://api.generadordni.es/v2/text/words?words=1&language=es'

WORDS = []

for i in range(0, 4):
    response = requests.get(url)
    response_json = response.json()
    WORDS.extend(response_json)

print('Espere...')
print(WORDS)