CREATE EXTERNAL TABLE IF NOT EXISTS `stedi-project-db`.`customer_curated` (
  `serialNumber` string,
  `birthDay` string,
  `shareWithResearchAsOfDate` bigint,
  `registrationDate` bigint,
  `customerName` string,
  `shareWithFriendsAsOfDate` bigint,
  `email` string,
  `lastUpdateDate` bigint,
  `phone` string,
  `shareWithPublicAsOfDate` bigint
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
WITH SERDEPROPERTIES (
  'ignore.malformed.json' = 'FALSE',
  'dots.in.keys' = 'FALSE',
  'case.insensitive' = 'TRUE',
  'mapping' = 'TRUE'
)
STORED AS INPUTFORMAT 'org.apache.hadoop.mapred.TextInputFormat' OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION 's3://stedi-project-makni/customer/curated/'
TBLPROPERTIES ('classification' = 'json');