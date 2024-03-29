import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql import functions as SqlFuncs

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node customer trusted
customertrusted_node1711640152458 = glueContext.create_dynamic_frame.from_options(format_options={"multiline": False}, connection_type="s3", format="json", connection_options={"paths": ["s3://stedi-project-makni/customer/trusted/"], "recurse": True}, transformation_ctx="customertrusted_node1711640152458")

# Script generated for node accelerometer landing
accelerometerlanding_node1711640154398 = glueContext.create_dynamic_frame.from_options(format_options={"multiline": False}, connection_type="s3", format="json", connection_options={"paths": ["s3://stedi-project-makni/accelerometer/landing/"], "recurse": True}, transformation_ctx="accelerometerlanding_node1711640154398")

# Script generated for node customer privacy filter
customerprivacyfilter_node1711640304670 = Join.apply(frame1=accelerometerlanding_node1711640154398, frame2=customertrusted_node1711640152458, keys1=["user"], keys2=["email"], transformation_ctx="customerprivacyfilter_node1711640304670")

# Script generated for node Drop Fields
DropFields_node1711640564094 = DropFields.apply(frame=customerprivacyfilter_node1711640304670, paths=["user", "timestamp", "x", "y", "z"], transformation_ctx="DropFields_node1711640564094")

# Script generated for node Drop Duplicates
DropDuplicates_node1711649869348 =  DynamicFrame.fromDF(DropFields_node1711640564094.toDF().dropDuplicates(["email"]), glueContext, "DropDuplicates_node1711649869348")

# Script generated for node Amazon S3
AmazonS3_node1711640633742 = glueContext.write_dynamic_frame.from_options(frame=DropDuplicates_node1711649869348, connection_type="s3", format="json", connection_options={"path": "s3://stedi-project-makni/customer/curated/", "partitionKeys": []}, transformation_ctx="AmazonS3_node1711640633742")

job.commit()