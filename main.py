import json, pytz
from datetime import date, timedelta, datetime
from line_utils import send_line
from bigquery_utils import run_query


with open('config.json') as f: config = json.load(f)
date_format = "%Y-%B-%d"
datetime_today = datetime.now(pytz.timezone('Asia/Bangkok'))
today = datetime_today.strftime(date_format)

def process_data(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
    """
    date_text = config['date_text'].format(today)
    line_notify_token = config["line_notify_token"]
    
