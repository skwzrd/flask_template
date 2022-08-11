from datetime import datetime
import os

def make_date(val):
    d = datetime.fromisoformat(val)
    return d.strftime('%b %d, %Y %I:%M %p').replace(' AM', 'am').replace(' PM', 'pm')

def make_path(*filename):
    directory = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(directory, *filename)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    return os.path.abspath(path)
