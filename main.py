import json, pytz, os
from datetime import date, timedelta, datetime
from utils import BigQueryUtils, LineUtils

#region reading config 
with open('./private/config.json') as f: config = json.load(f)
cfg_reports = config['report']
billing_project = config['billing']['project']
billing_dateset = config['billing']['dateset']
billing_table = config['billing']['table']
#endregion reading config 

if 'GAE_ENV' in os.environ and str(os.environ['GAE_ENV']).lower() == 'standard':
    """ If running enviroment is GCF, using service account configuration. """
    pass
else: os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = config['gcp_credetials']

def process_data(request):
    """
    Read config and run SQL on BigQuery to get daily report status and send line notify.
    """

    date_format = "%Y-%B-%d"
    datetime_today = datetime.now(pytz.timezone('Asia/Bangkok'))
    today = datetime_today.strftime(date_format)
    
    bq_utils = BigQueryUtils()
    line_utils = LineUtils(token=config["line_notify_token"])

    for cfg in cfg_reports:
        name = cfg["name"]
        message = cfg["message"]
        string_format = cfg['string_format']
        sql_file = cfg["sql_file"]
        with open(sql_file) as f: sql = f.read()
        sql = sql.format(project=billing_project, dataset=billing_dateset, table=billing_table)
        data = bq_utils.run_query(sql, string_format)
        message = '\n'.join(message)
        message = message.format(data=data,data_date=today)
        print(message)
        line_utils.send_line(message)
    
    return "Successfully send LINE Notify"
    
