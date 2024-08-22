from dlt.destinations import motherduck
import os

motherduck_credentials = {
    "database": os.getenv("MD_DATABASE"),
    "password": os.getenv("MD_TOKEN"),
}

aw_motherduck = motherduck(credentials=motherduck_credentials)
