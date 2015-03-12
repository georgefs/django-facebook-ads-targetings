#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2015 vagrant 
#
# Distributed under terms of the MIT license.
import facebook_login
facebook_login.initialize()
from facebookads.api import FacebookAdsApi
import copy



class BaseFacebookTargeting(object):
    key = ""
    classify = ""
    def __init__(self, key, search_params=[], classify=""):
        self.key=key
        self.search_params = search_params
        self.classify = classify

    def search(self, *args, **kwargs):
        pass
    
    def search_params(self, *args, **kwargs):
        return self.search_params

    def __repr__(self):
        return "<FacebookTargeting:{}>".format( self.key)


fbapi = FacebookAdsApi.get_default_api()
class APIFacebookTargeting(BaseFacebookTargeting):
    path = ["search"]
    method = "POST"
    base_attrs = {}
    def __init__(self, opt_key, opt_value, path=["search"], method="GET", base_attrs={}, *args, **kwargs):
        self.path = path
        self.method = method.upper().strip()
        self.base_attrs.update(base_attrs)
        self.opt_key = opt_key
        self.opt_value = opt_value
        assert self.method in ('GET', 'POST', 'PUT', 'DELETE')
        super(APIFacebookTargeting, self).__init__(*args, **kwargs)
        pass

    def parser_value(self, data):
        if isinstance(self.opt_value, basestring):
            return data.get(self.opt_value)
        result = {}
        for key in self.opt_value:
            if isinstance(key, basestring):
                result[key] = data[key]
            elif isinstance(key, dict):
                old_key, new_key = key.items()[0]
                result[new_key] = data[old_key]

        return result


    def search(self, *args, **kwargs):
        params = copy.deepcopy(self.base_attrs)
        params.update(kwargs)
        result = fbapi.call(method=self.method, path=self.path, params = params)
        return result.json()

    def options(self, *args, **kwargs):
        data = self.search(*args, **kwargs)['data']
        options = [{"name": v[self.opt_key], "value": self.parser_value(v)} for v in data]
        return options



class SimpleFacebookTargeting(BaseFacebookTargeting):
    _options = ()
    def __init__(self, options=(), *args, **kwargs):
        super(SimpleFacebookTargeting, self).__init__(*args, **kwargs)
        self._options = options

    def search(self):
        return self._options

    def options(self):
        return self._options


class AdCategoryTargeting(APIFacebookTargeting):
    method = "POST"
    base_attrs = {"class":"", "type":"adTargetingCategory"}
    def __init__(self, key, method="GET", opt_key="name", opt_value=["id", "name"], *args, **kwargs):
        self.base_attrs['class'] = key
        super(AdCategoryTargeting, self).__init__(key=key, method=method, opt_key=opt_key, opt_value=opt_value, *args, **kwargs)
        self.base_attrs = copy.deepcopy(self.base_attrs)
