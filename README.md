why
---
facebook ads targeting 的結構還頗複雜.. 我們又需要把targeting 的選項拿出來, 所以特別做這包


install
---

```bash
git clone git@github.com:georgefs/django-facebook-ads-targetings.git
cd django-facebook-ads-targetings
python setup.py install
```

usage
---
https://developers.facebook.com/docs/marketing-api/targeting-specs/v2.2#interests

拿interests 的targeting 來做範例

```python
In [1]: from facebook_ads_targetings import *

In [2]: interests_targeting = get_targeting('interests')

In [3]: print interests_targeting
<FacebookTargeting:interests>

In [4]: print interests_targeting.search()  ## 用 v2.2/search api query facebook 的結果
{u'data': [{u'path': [u'Shopping and fashion', u'Beauty', u'Cosmetics'], u'audience_size': 336332120, u'type': u'interests', u'id': u'6002839660079', u'name': u'Cosmetics'} .... ] 

In [5]: print interests_targeting.options()  ## 取AdSet 的 interests 的 targeting 設定 "Array of objects with 'id' and 'name' fields. eg; 'interests':[{id: 6003139266461, 'name': 'Movies'}]"
[{'name': u'Cosmetics', 'value': {'id': u'6002839660079', 'name': u'Cosmetics'}}, {'name': u'Science', 'value': {'id': u'6002866718622', 'name': u'Science'}} ... ]

```

search 就是 search api 後的result
option 就是把search 後的結果取出 adset targeting 設定的部分, 並做成[{key:key, value:value}, ..] 方便做option


