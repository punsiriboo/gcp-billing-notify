import json
from google.cloud import bigquery


class BigQueryUtils:
    def __init__(self):
        self.client = bigquery.Client()
        
    def run_query(self, query_string, farmat_pattern='%s: %s$'):
        query_job = self.client.query(query_string)
        query_job.result()
        df = query_job.to_dataframe()
        values = json.loads(df.to_json(orient="values")) if len(df) > 0 else []
        print(values)
        data_text = '\n'.join(farmat_pattern % tuple(v) for v in values)
        return data_text