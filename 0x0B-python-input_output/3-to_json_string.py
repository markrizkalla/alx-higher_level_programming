#!/usr/bin/python3
"""Define fun that return the JSON repr"""
import json


def to_json_string(my_obj):
    """return json repre of my_boj"""
    return json.dumps(my_obj)
