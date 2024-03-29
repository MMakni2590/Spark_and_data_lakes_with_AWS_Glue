import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node step trainer landing
steptrainerlanding_node1711702599002 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiLine": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://stedi-project-makni/step_trainer/landing/"],
        "recurse": True,
    },
    transformation_ctx="steptrainerlanding_node1711702599002",
)

# Script generated for node customers curated
customerscurated_node1711702533811 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiLine": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://stedi-project-makni/customer/curated/"],
        "recurse": True,
    },
    transformation_ctx="customerscurated_node1711702533811",
)

# Script generated for node Join
Join_node1711703347763 = Join.apply(
    frame1=customerscurated_node1711702533811,
    frame2=steptrainerlanding_node1711702599002,
    keys1=["serialNumber"],
    keys2=["serialNumber"],
    transformation_ctx="Join_node1711703347763",
)

# Script generated for node Drop Fields
DropFields_node1711704275728 = DropFields.apply(
    frame=Join_node1711703347763,
    paths=[
        "shareWithFriendsAsOfDate",
        "shareWithPublicAsOfDate",
        "phone",
        "lastUpdateDate",
        "email",
        "customerName",
        "registrationDate",
        "shareWithResearchAsOfDate",
        "birthDay",
        "serialNumber",
    ],
    transformation_ctx="DropFields_node1711704275728",
)

# Script generated for node step trainer trusted
steptrainertrusted_node1711704311144 = glueContext.write_dynamic_frame.from_options(
    frame=DropFields_node1711704275728,
    connection_type="s3",
    format="json",
    connection_options={
        "path": "s3://stedi-project-makni/step_trainer/trusted/",
        "compression": "snappy",
        "partitionKeys": [],
    },
    transformation_ctx="steptrainertrusted_node1711704311144",
)

job.commit()
