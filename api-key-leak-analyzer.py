import re
import requests

database_clean = []

def find_api_keys(link):

    api_keys = []
  
    response = requests.get(url=link)

    pattern = re.compile(r'(\b(?=\w*\d)(?=\w*[a-zA-Z])[a-zA-Z\d]{10,}\b)')
    matches = re.findall(pattern, response.text)
    api_keys.extend(matches)

    for palavra in api_keys:

      if palavra not in database_clean:
        print(palavra)
        database_clean.append(palavra)

    return database_clean


api_keys = find_api_keys("https://teste.com.br/exemplo.js")

with open("limpo.txt", 'w') as out_file:
    out_file.write("\n".join(api_keys))
