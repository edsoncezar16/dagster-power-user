from dagster_embedded_elt.sling import (
    SlingConnectionResource,
    SlingResource,
)
from dagster_embedded_elt.dlt import DagsterDltResource

from dagster import EnvVar

source = SlingConnectionResource(
    name="AW_S3",
    type="s3",
    bucket=EnvVar("S3_BUCKET"),
    access_key_id=EnvVar("AWS_ACCESS_KEY_ID"),
    secret_access_key=EnvVar("AWS_SECRET_ACCESS_KEY"),
)

target = SlingConnectionResource(
    name="AW_MD",
    type="motherduck",
    database=EnvVar("MD_DATABASE"),
    motherduck_token=EnvVar("MD_TOKEN")
)

sling = SlingResource(
    connections=[
        source,
        target,
    ]
)

dlt = DagsterDltResource()
