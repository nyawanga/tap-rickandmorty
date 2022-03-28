"""Stream type classes for tap-rickandmorty."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_rickandmorty.client import RickAndMortyStream

# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")
# TODO: - Override `UsersStream` and `GroupsStream` with your own stream definition.
#       - Copy-paste as many times as needed to create multiple stream types.


class CharacterStream(RickAndMortyStream):
    """Define custom stream."""

    name = "character"
    path = "/character"
    primary_keys = ["id"]
    # replication_key = None
    replication_key = "id"
    replicaton_method = "INCREMENTAL"
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    # schema_filepath = SCHEMAS_DIR / "users.json"
    schema = th.PropertiesList(
        th.Property("name", th.StringType),
        th.Property("id", th.IntegerType, description="The user's system ID"),
        th.Property(
            "status", th.StringType, description="The user's live status Alive or Dead"
        ),
        th.Property("species", th.IntegerType, description="The user's age in years"),
        th.Property("type", th.StringType, description="The user's email address"),
        th.Property("gender", th.StringType),
        # th.Property("origin", Dict),
        # th.Property(
        #     "location", th.ObjectType, description="State name in ISO 3166-2 format"
        # ),
        th.Property("url", th.StringType, description="url of the character"),
        th.Property(
            "image", th.StringType, description="The image url for the character"
        ),
        # th.Property("episode", th.ArrayType),
        th.Property("created", th.DateTimeType),
    ).to_dict()


# class GroupsStream(RickAndMortyStream):
#     """Define custom stream."""

#     name = "groups"
#     path = "/groups"
#     primary_keys = ["id"]
#     replication_key = "modified"
#     schema = th.PropertiesList(
#         th.Property("name", th.StringType),
#         th.Property("id", th.StringType),
#         th.Property("modified", th.DateTimeType),
#     ).to_dict()
