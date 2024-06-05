import base64
from jwt.exceptions import ExpiredSignatureError
import jwt



def decode_user(token: str):
    header_data = jwt.get_unverified_header(token)
    print(header_data)
    try:
        payload = jwt.decode(
        token,
        key='my_super_secret',
        algorithms=[header_data['alg'], ]
    )
        return payload.get('name')
    except ExpiredSignatureError as error:
        print(f'Unable to decode the token, error: {error}')

payload_data = {
    "sub": "4242",
    "name": "user1",
    "nickname": "Jess"
}

my_secret = 'my_super_secret'

token = jwt.encode(
    payload=payload_data,
    key=my_secret
)

print(token)
username = decode_user(token)
print(f"Extracted username: {username}")
