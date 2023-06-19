import secrets
import datetime
import base64

class key:

    value = secrets.token_urlsafe(24)
    salt = (base64.b64encode(secrets.token_bytes(nbytes=16))).decode('ascii')
    timestamp = datetime.datetime.now(datetime.timezone.utc)