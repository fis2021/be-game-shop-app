from rest_framework_jwt.utils import jwt_payload_handler


def payload_handler(user):
    payload = jwt_payload_handler(user)
    payload['user_type'] = user.user_type
    return payload
