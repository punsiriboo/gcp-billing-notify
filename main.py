import json, pytz
from datetime import date, timedelta, datetime
from utils import BigQueryUtils, LineUtils


def process_data(request):
    """
    Read config and run SQL on BigQuery to get daily report status and send line notify.
    """

    date_format = "%Y-%B-%d"
    datetime_today = datetime.now(pytz.timezone('Asia/Bangkok'))
    today = datetime_today.strftime(date_format)

    #region reading config 
    with open('config.json') as f: config = json.load(f)
    cfg_reports = config['report']
    billing_project = config['billing']['project']
    billing_dateset = config['billing']['dateset']
    billing_table = config['billing']['table']
    #endregion reading config 
    
    bq_utils = BigQueryUtils()
    line_utils = LineUtils(token=config["line_notify_token"])

    for cfg in cfg_reports:
        name = cfg["name"]
        message = cfg["message"]
        sql_file = cfg["sql_file"]
        with open(sql_file) as f: sql = f.read()
        sql.format(project=billing_project, dataset=billing_dateset, table=billing_table)
        data = bq_utils.run_query(sql)
        line_utils.send_line()
    
