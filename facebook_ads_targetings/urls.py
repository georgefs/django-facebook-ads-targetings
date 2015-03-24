#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2015 vagrant 
#
# Distributed under terms of the MIT license.
from django.conf.urls import patterns, url
from facebook_ads_targetings import views

urlpatterns = patterns('',
    url(r'^$', 'facebook_ads_targetings.views.index'),
    url(r'^targetings$', 'facebook_ads_targetings.views.targetings', name='targetings'),
    url(r'^targetings/(?P<type_name>\w+)/options$', 'facebook_ads_targetings.views.options', name='targeting_options')
)

