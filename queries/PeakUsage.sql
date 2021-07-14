WITH last_7day_usage as (
    SELECT DATE(usage_start_time) as date, round(sum(cost),2) as cost
    FROM `{project}.{dataset}.{table}`
    WHERE  DATE(usage_start_time) BETWEEN DATE_SUB(DATE("2019-10-17"), INTERVAL 8 DAY) AND DATE_SUB(DATE("2019-10-17"), INTERVAL 2 DAY)
    group by 1
),
avg_last_7day_usage as (
    SELECT avg(cost) as avg_cost from last_7day_usage
),
today_usage as (
    SELECT round(sum(cost),2) as cost
    FROM `{project}.{dataset}.{table}`
    WHERE DATE(usage_start_time) = DATE_SUB(DATE("2019-10-17"), INTERVAL 1 DAY)
)

select round(cost/avg_cost,2) as warning_threshold, round(avg_cost,2) from today_usage, avg_last_7day_usage