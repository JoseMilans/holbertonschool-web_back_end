#!/usr/bin/env python3
"""Module for updating topics in MongoDB school documents
"""


def update_topics(mongo_collection, name, topics):
    """Changes all topics of a school document based on the name
    """
    query = {"name": name}
    new_values = {"$set": {"topics": topics}}
    result = mongo_collection.update_many(query, new_values)
    return result.matched_count
