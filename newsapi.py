# -*- coding: utf-8 -*-
"""
Example module that says 'Hello World!'

This demonstrates how to produce a simple custom module.
"""

import json
import requests
import time

class Py3status:
    def newsapi(self):
        api_key = 'fe99f0fd7ee74c3887cdcb0fef3ede0a'
        source = 'techcrunch'
        params = {'source':source, 'apiKey':api_key}
        response = requests.get('https://newsapi.org/v1/articles', params=params)
        parsed = json.loads(response.text)
        #
        titles = ''
        for article in parsed['articles']:
            titles += article['title']+'. '
        i = int(time.time()*10)%len(titles)
        titles = titles[i:]+titles[:i]
        titles = titles[:35]
        return {'full_text': source+': '+titles, 'cached_until': .1}
        #article =  int(time.time()/30)%len(parsed['articles'])
        #title = parsed['articles'][article]['title']+'. '
        ##title = parsed['articles'][0]['title']+'. '
        #i = int(time.time())%len(title)
        #return {'full_text': source+': '+title[i:]+title[:i], 'cached_until': 1}
        #return {
        #    'full_text': result,
        #    'cached_until': .5
        #}

if __name__ == "__main__":
    """
    Run module in test mode.
    """
    from py3status.module_test import module_test
    module_test(Py3status)
