from datetime import datetime


class DateUrlConverter:
    regex = '\d{2}\.\d{2}\.\d{4}'

    def to_python(self, value):
        return datetime.strptime(value, '%d.%m.%Y')
