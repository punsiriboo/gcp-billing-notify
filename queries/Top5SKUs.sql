SELECT
CONCAT(project.name, "'s ", SUBSTR(sku.description, 1, 20)) AS sku_description, 
round(sum(cost),2) as cost
FROM `{project}.{dataset}.{table}`
WHERE DATE(usage_start_time) = DATE_SUB(DATE("2019-10-17"), INTERVAL 1 DAY
group by  1
order by 2 desc limit 5