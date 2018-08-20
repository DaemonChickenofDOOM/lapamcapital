#!/usr/bin/python3

import requests
my_domain = 'Vostok.pythonanywhere.com'
username = 'Vostok'
token = 'e5866b7144d5f32e4d58c22cef2deab9c0a95403'

response = requests.post(
    'https://www.pythonanywhere.com/api/v0/user/{username}/webapps/{domain}/reload/'.format(
        username=username, domain=my_domain
    ),
    headers={'Authorization': 'Token {token}'.format(token=token)}
)
if response.status_code == 200:
    print('All OK')
else:
    print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))