#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
from typing import Any, Dict

import jmespath
import rich
from dotty_dict import dotty

for_extract_str = {
    "name": "China",
    "population": 1431002651,
    "capital": "Beijing",
    "languages": [
        "Chinese"
    ],"students": {
        "name": "name",
        "age":18
    }
}

json_str = """
{
    "name": "China",
    "population": 1431002651,
    "capital": "Beijing",
    "languages": [
        "Chinese"
    ],"students": {
        "name": "name",
        "age":18
    }
}
"""

for_extract_str = {
    "name": "China",
    "population": 1431002651,
    "capital": "Beijing",
    "languages": [
        "Chinese"
    ],"students": {
        "name": "name",
        "age":18
    }
}

def get_value(json_str: Dict, path_exp: str) -> Any:
    return jmespath.search(expression=path_exp, data=json_str)


def set_value(json_dict: Dict, path_exp: str, to_value: Any) -> Dict:
    dot = dotty(json_dict)
    dot[path_exp] = to_value
    return dot.to_dict()


rich.print(set_value(json_dict=for_extract_str, path_exp="languages",
                     to_value=["None", "OK"]))
rich.print(get_value(json_str=for_extract_str, path_exp="languages"))

rich.print(set_value(json_dict=for_extract_str, path_exp="students.name",
                     to_value="Niu"))
rich.print(get_value(json_str=json.loads(json_str), path_exp="students.name"))
rich.print(get_value(json_str=for_extract_str, path_exp="students.name"))
