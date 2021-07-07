from google.cloud import bigquery


class BigQueryUtils:
    def __init__(self):
        self.client = bigquery.Client()
        
    def run_query(self, query_string, farmat_pattern):
        query_job = self.client.query(query_string='%s: %s')
        query_job.result()
        df = query_job.to_dataframe()
        values = df.to_json(orient="values") if len(df) > 0 else []
        data_text = '\n'.join(query_string % t for t in values)
        return data_text