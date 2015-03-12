#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2015 vagrant 
#
# Distributed under terms of the MIT license.
# opt_value = list 則 option 的value 要為 dict
# opt_key = search 的 key

from base import APIFacebookTargeting, SimpleFacebookTargeting, AdCategoryTargeting, BaseFacebookTargeting




#https://developers.facebook.com/docs/marketing-api/targeting-specs/v2.2#demographics
genders = SimpleFacebookTargeting(
                classify="demographics",
                key="genders", 
                options=({"name": "male", "value": 1}, {"name": "female", "value": 2}),
            )

age_min = SimpleFacebookTargeting(
                classify="demographics",
                key="age_min", 
                search_params="__noopt",
            )

age_max = SimpleFacebookTargeting(
                classify="demographics",
                key="age_max", 
                search_params="__noopt",
            )


#https://developers.facebook.com/docs/marketing-api/targeting-specs/v2.2#location
countries = APIFacebookTargeting(
                classify="geo_locations",
                key="geo_locations__countries", 
                base_attrs={"location_types":"['country']", "type":"adgeolocation"},
                search_params=[{"q": "The string for which you want autocomplete values"}],
                opt_key="name",
                opt_value="key"
            )

regions = APIFacebookTargeting(
                classify="geo_locations",
                key="geo_locations__regions", 
                base_attrs={"location_types":"['country']", "type":"adgeolocation"},
                search_params=[{"q": "The string for which you want autocomplete values"}],
                opt_key="name",
                opt_value=["key"]
            )

zips = APIFacebookTargeting(
                classify="geo_locations",
                key="geo_locations__zips", 
                base_attrs={"location_types":"['zip']", "type":"adgeolocation"},
                search_params=[{"q": "search for all zip that start with text"}],
                opt_key="name",
                opt_value=["key"]
            )

geo_markets = APIFacebookTargeting(
                classify="geo_locations",
                key="geo_locations__geo_markets", 
                base_attrs={"location_types":"['geo_market']", "type":"adgeolocation"},
                search_params=[{"q": "To search for DMA codes that are targetable on Facebook specify"}],
                opt_key="name",
                opt_value=["key"]
            )

location_types = SimpleFacebookTargeting(
                classify="geo_locations",
                key="geo_locations__geo_location_types", 
                options=({"name": "recent", "value": "recent"}, {"name": "home", "value": "home "}, {"name": "travel_in", "value": "travel_in"}),
            )

#https://developers.facebook.com/docs/marketing-api/targeting-specs/v2.2#mobile
user_os = SimpleFacebookTargeting(
                classify="mobile",
                key="user_os", 
                options=({"name":"android", "value": "android"}, {"name": "iOS", "value": "iOS"}),
            )

user_device = AdCategoryTargeting(
                classify="mobile",
                key="user_device", 
                opt_value="name"
            )

#wireless_carrier

#site_category


#https://developers.facebook.com/docs/marketing-api/targeting-specs/v2.2#placement
page_types = SimpleFacebookTargeting(
                classify="placement",
                key="page_types", 
                options=(
                        {"name": "desktop", "value": "desktop"},
                        {"name": "feed", "value": "feed"},
                        {"name": "desktopfeed", "value": "desktopfeed"},
                        {"name": "rightcolumn", "value": "rightcolumn"},
                        {"name": "rightcolumn-and-mobile", "value": "rightcolumn-and-mobile"},
                        {"name": "home", "value": "home"},
                        {"name": "mobilefeed-and-external", "value": "mobilefeed-and-external"},
                        {"name": "desktop-and-mobile-and-external", "value": "desktop-and-mobile-and-external"},
                        {"name": "feed-and-external", "value": "feed-and-external"},
                        {"name": "rightcolumn-and-mobile-and-external", "value": "rightcolumn-and-mobile-and-external"},
                    ),
            )



#https://developers.facebook.com/docs/marketing-api/targeting-specs/v2.2#facebook_connections
#connections

#excluded_connections

#friends_of_connections


#https://developers.facebook.com/docs/marketing-api/targeting-specs/v2.2#interests
interests = AdCategoryTargeting(
                classify="interests",
                key="interests", 
            )

#https://developers.facebook.com/docs/marketing-api/targeting-specs/v2.2#behaviors
user_device = AdCategoryTargeting(
                classify="behaviors",
                key="behaviors", 
            )

#https://developers.facebook.com/docs/marketing-api/targeting-specs/v2.2#advanced_demographics
relationship_statuses = SimpleFacebookTargeting(
                classify="advanced_demographics",
                key="relationship_statuses", 
                options=(
                        {"name": "single", "value": 1},
                        {"name": "in_relationship", "value": 2},
                        {"name": "married", "value": 3},
                        {"name": "engaged", "value": 4},
                        {"name": "not specified", "value": 6},
                        {"name": "in a civil union", "value": 7},
                        {"name": "in a domestic partnership", "value": 8},
                        {"name": "In an open relationship", "value":9},
                        {"name": "It's complicated", "value": 10},
                        {"name": "Separated", "value": 11},
                        {"name": "Divorced", "value":12},
                        {"name": "Widowed", "value": 13},
                    ),
            )

interested_in = SimpleFacebookTargeting(
                classify="advanced_demographics",
                key="interested_in", 
                options=(
                        {"name": "men", "value": 1},
                        {"name": "women", "value": 2},
                        {"name": "men and women", "value": 3},
                        {"name": "not specified", "value": 4},
                    ),
            )

life_events = AdCategoryTargeting(
                classify="advanced_demographics",
                key="life_events", 
            )

politics = AdCategoryTargeting(
                classify="advanced_demographics",
                key="politics", 
            )

markets = AdCategoryTargeting(
                classify="advanced_demographics",
                key="markets", 
            )

industries = AdCategoryTargeting(
                classify="advanced_demographics",
                key="industries", 
            )

income = AdCategoryTargeting(
                classify="advanced_demographics",
                key="income", 
            )

net_worth = AdCategoryTargeting(
                classify="advanced_demographics",
                key="net_worth", 
            )


home_type = AdCategoryTargeting(
                classify="advanced_demographics",
                key="home_type", 
            )

home_ownership = AdCategoryTargeting(
                classify="advanced_demographics",
                key="home_ownership", 
            )

home_value = AdCategoryTargeting(
                classify="advanced_demographics",
                key="home_value", 
            )

ethnic_affinity = AdCategoryTargeting(
                classify="advanced_demographics",
                key="ethnic_affinity", 
            )

generation = AdCategoryTargeting(
                classify="advanced_demographics",
                key="generation", 
            )

household_composition = AdCategoryTargeting(
                classify="advanced_demographics",
                key="household_composition", 
            )

moms = AdCategoryTargeting(
                classify="advanced_demographics",
                key="moms", 
            )

office_type = AdCategoryTargeting(
                classify="advanced_demographics",
                key="office_type", 
            )


#https://developers.facebook.com/docs/marketing-api/targeting-specs/v2.2#education_and_workplace
education_schools = APIFacebookTargeting(
                classify="education_and_workplace",
                key="education_schools", 
                base_attrs={"type":"adeducationschool"},
                search_params=[{"q": "search for all schools that start with text"}],
                opt_key="name",
                opt_value=[{"key": "id"}, "name"]
            )

education_statuses = SimpleFacebookTargeting(
                classify="education_and_workplace",
                key="education_statuses", 
                options=(
                        {"name": "HIGH_SCHOOL", "value":1},
                        {"name": "UNDERGRAD", "value":2},
                        {"name": "ALUM", "value":3},
                        {"name": "HIGH_SCHOOL_GRAD", "value":4},
                        {"name": "SOME_COLLEGE", "value":5},
                        {"name": "ASSOCIATE_DEGREE", "value":6},
                        {"name": "IN_GRAD_SCHOOL", "value":7},
                        {"name": "SOME_GRAD_SCHOOL", "value":8},
                        {"name": "MASTER_DEGREE", "value":9},
                        {"name": "PROFESSIONAL_DEGREE", "value":10},
                        {"name": "DOCTORATE_DEGREE", "value":11},
                        {"name": "UNSPECIFIED", "value":12},
                        {"name": "SOME_HIGH_SCHOOL", "value":13},
                    ),
            )

college_years = APIFacebookTargeting(
                classify="education_and_workplace",
                key="college_years", 
                search_params="__noopt",
                opt_key="name",
                opt_value=["key"]
            )

education_majors = APIFacebookTargeting(
                classify="education_and_workplace",
                key="education_majors", 
                base_attrs={"type":"adeducationmajor"},
                search_params=[{"q": "For example to search for all education majors that start with text"}],
                opt_key="name",
                opt_value=[{"key": "id"}, "name"]
            )

work_employers = APIFacebookTargeting(
                classify="education_and_workplace",
                key="work_employers", 
                base_attrs={"type":"adworkemployer"},
                search_params=[{"q": "For example to search for all education majors that start with text"}],
                opt_key="name",
                opt_value=[{"key": "id"}, "name"]
            )

work_positions = APIFacebookTargeting(
                classify="education_and_workplace",
                key="work_positions", 
                base_attrs={"type":"adworkposition"},
                search_params=[{"q": "For example to search for all education majors that start with text"}],
                opt_key="name",
                opt_value=[{"key": "id"}, "name"]
            )

locales = APIFacebookTargeting(
                classify="education_and_workplace",
                key="locales", 
                base_attrs={"type":"adlocale"},
                search_params=[{"q": "The string for which you want autocomplete values"}],
                opt_key="name",
                opt_value="key"
            )

#https://developers.facebook.com/docs/marketing-api/targeting-specs/v2.2#broadcategories
user_adclusters = APIFacebookTargeting(
                classify="broadcategories",
                key="user_adclusters", 
                search_params=[{"q": "The string for which you want autocomplete values"}],
                opt_key="name",
                opt_value=[{"key": "id"}, "name"]
            )


user_adclusters = APIFacebookTargeting(
                classify="broadcategories",
                key="user_adclusters", 
                search_params=[{"q": "The string for which you want autocomplete values"}],
                opt_key="name",
                opt_value=[{"key": "id"}, "name"]
            )

__all__ = [k for k, v in locals().items() if isinstance(v, BaseFacebookTargeting)]
