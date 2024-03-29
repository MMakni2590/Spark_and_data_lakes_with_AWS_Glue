import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
import re

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node customer landing
customerlanding_node1711635477162 = glueContext.create_dynamic_frame.from_options(format_options={"multiline": False}, connection_type="s3", format="json", connection_options={"paths": ["s3://stedi-project-makni/customer/landing/"], "recurse": True}, transformation_ctx="customerlanding_node1711635477162")

# Script generated for node share_with_researrch
share_with_researrch_node1711635591213 = Filter.apply(frame=customerlanding_node1711635477162, f=lambda row: (not(row["shareWithResearchAsOfDate"] == 0)), transformation_ctx="share_with_researrch_node1711635591213")

# Script generated for node customer trusted
customertrusted_node1711636052433 = glueContext.write_dynamic_frame.from_options(frame=share_with_researrch_node1711635591213, connection_type="s3", format="json", connection_options={"path": "s3://stedi-project-makni/customer/trusted/", "compression": "snappy", "partitionKeys": []}, transformation_ctx="customertrusted_node1711636052433")

job.commit()