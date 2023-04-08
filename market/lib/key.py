import secrets, string, uuid, datetime

a = string.ascii_letters + string.digits + string.punctuation

class key:

    uuid = uuid.uuid4()
    value = ''.join(secrets.choice(a) for i in range(64))
    timestamp = datetime.datetime.now(datetime.timezone.utc)
