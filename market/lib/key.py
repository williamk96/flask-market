import secrets, uuid, datetime

class key:

    uuid = uuid.uuid4()
    value = secrets.token_urlsafe(24)
    timestamp = datetime.datetime.now(datetime.timezone.utc)