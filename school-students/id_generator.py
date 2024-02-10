import random

CHARS = "1234567890"


def generate_uuid(length: int = 4) -> str:
    random_chars = [random.choice(CHARS) for _ in range(length)]
    result = "".join(random_chars)
    return result


uuid = generate_uuid()
# print(uuid)
