gcloud functions deploy gcp-billing-notify\
    --entry-point=process_data\
    --set-env-vars=GAE_ENV=standard\
    --service-account=$SERVICE_ACCOUNT