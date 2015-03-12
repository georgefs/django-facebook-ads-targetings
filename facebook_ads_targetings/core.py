#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2015 vagrant 
#
# Distributed under terms of the MIT license.

import targetings

def get_types():
    result = []
    for targeting_name in targetings.__all__:
        targeting = getattr(targetings, targeting_name)
        data = {}
        data["name"] = targeting_name
        data["attrs"] = targeting.search_params
        data["classify"] = targeting.classify
        result.append(result)
    return result

def get_options(targeting_name, search_params={}):
    return get_targeting(targeting_name).options(**search_params)

def get_targeting(targeting_name):
    return getattr(targetings, targeting_name)


