#!/usr/bin/env python3
"""Module for inserting a document into a MongoDB collection
"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document into a collection
    """
    new_doc = mongo_collection.insert_one(kwargs)
    return new_doc.inserted_id
