import secrets


PW_LENGTH = 10
PW_CHARSET = 'ABCDEFGHIJKLMNPQRSTUVWXYZ' \
             'abcdefghijklmnopqrstuvwxyz' \
             '0123456789' \
             '!@#$%^&*-+_'


# Генерирует надежный пароль
def gen_password(length=PW_LENGTH, charset=PW_CHARSET):
    return ''.join([secrets.choice(charset) for _ in range(0, length)])
