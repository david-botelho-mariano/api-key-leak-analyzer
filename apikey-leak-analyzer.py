import re

database_clean = []

def find_api_keys(file_path):

    api_keys = []

    with open(file_path, 'r') as file:

        contents = file.read()
        pattern = re.compile(r'(\b(?=\w*\d)(?=\w*[a-zA-Z])[a-zA-Z\d]{10,}\b)')
        matches = re.findall(pattern, contents)
        api_keys.extend(matches)
        print(api_keys)

        for palavra in api_keys:

          if palavra not in database_clean:

            database_clean.append(palavra)


    return database_clean


# Example usage
api_keys = find_api_keys("1.js")

# Saving the API keys to a file
with open("limpo.txt", 'w') as out_file:
    out_file.write("\n".join(api_keys))

