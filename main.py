from db import get_data
from emailer import send_email

data = get_data()
send_email(data)
