import hashlib
import requests
import json


def gravatar(email):
    url = 'https://ru.gravatar.com/'

    email_md5 = hashlib.md5(email.encode('utf-8')).hexdigest()
    data = requests.get(url + email_md5 + '.json').json()

    return data


def rename(json_data):
    data = json_data['entry'][0]
    new_dict = {
        'id': data.get('id'),
        'email_hash': data.get('hash'),
        'url': data.get('profileUrl'),
        'alias': data.get('preferredUsername'),
        'thumb': data.get('thumbnailUrl'),
        'photos': data.get('photos'),
        'person': data.get('name.formatted'),
        'location': data.get('currentLocation'),
        'emails': data.get('emails'),
        'accounts': data.get('accounts'),
        'urls': data.get('urls')
    }

    return {'result': new_dict}


def main(query):
    return rename(gravatar(query))


if __name__ == '__main__':
    print(json.dumps(main(input('query: ')), indent=4))
