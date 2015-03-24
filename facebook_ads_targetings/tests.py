from mock import patch
from django.test import TestCase
import facebook_ads_targetings

class myTest(TestCase):
    
    def test(self):
        
        with patch.object(facebook_ads_targetings.core, 'get_targeting') as mock_method:
            
            mock_method.options.return_value = [{'name': u'Cosmetics', 'value': {'id': u'6002839660079', 'name': u'Cosmetics'}}, {'name': u'Science', 'value': {'id': u'6002866718622', 'name': u'Science'}}, {'name': u'Beauty', 'value': {'id': u'6002867432822', 'name': u'Beauty'}}, {'name': u'Adventure travel', 'value': {'id': u'6002868021822', 'name': u'Adventure travel'}}, {'name': u'Organic food', 'value': {'id': u'6002868910910', 'name': u'Organic food'}}, {'name': u'Small business', 'value': {'id': u'6002884511422', 'name': u'Small business'}}]
            
            real = facebook_ads_targetings
            real.get_options('interests')
            
        mock_method.assert_called_once_with('interests')

    def test2(self):
        with patch.object(facebook_ads_targetings.core, 'get_targeting') as mock_method:
            mock_method.search_params .return_value= []
            mock_method.classify.return_value = 'interests'
            mock_method.options.return_value = [{'name': 'user_device', 'classify': 'behaviors', 'attrs': []}, {'name': 'home_ownership', 'classify': 'advanced_demographics', 'attrs': []}, {'name': 'education_statuses', 'classify': 'education_and_workplace', 'attrs': []}, {'name': 'location_types', 'classify': 'geo_locations', 'attrs': []}]

            real = facebook_ads_targetings
            real.get_types()

        mock_method.assert_called()
