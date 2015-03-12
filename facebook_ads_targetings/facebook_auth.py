#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2015 vagrant 
#
# Distributed under terms of the MIT license.


from facebookads.api import FacebookAdsApi
from facebookads import objects

my_app_id = '282445061933560'
my_app_secret = '965233bdcc5b208b0a33b534ff617e2a'
my_access_token = 'CAAEA4d2VyfgBAAhEydPuRkN6g6hWFLBYqOJEZBwpRoq6jdjMdrZAldCZAZAgnkSd9Idagt24FDpAZBn63nWAITUjvO6D6fBUhYdZCPN2BcJyEfpHOowgPzUpAPihz0gWdvapfvVtcswZBF7VHnlpcfzmmSc940ZC217Y86v9pZBoYZBkVklEDr1hPJTW77G9uwt1PxqHv7J2xHLtYkZBepbIYlZB'
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)



