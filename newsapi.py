# -*- coding: utf-8 -*-
"""
Module that displays news items from newsapi

This makes too many requests.
"""

import json
import requests
import time

class Py3status:
    #cache_timeout = 1 
    api_key = '<key>'
    sources = ['techcrunch', 'hacker-news', 'recode']
    source_switch_interval = 30
    scroll_multiplier = 10

    def _get_news(self):
        source = self.sources[int(time.time()/self.source_switch_interval)%len(self.sources)]
        params = {'source':source, 'apiKey':self.api_key}
        response = requests.get('https://newsapi.org/v1/articles', params=params)
        parsed = json.loads(response.text)
        return source, parsed

    def newsapi(self):
        source, parsed = self._get_news()
        titles = ''
        for article in parsed['articles']:
            titles += article['title']+'/ ' #too much trouble to use a period here as somtimes titles end in quoteds, i.e. doing +'. ' would leave a title ending '"<something>".' and that would not do.
        i = int(time.time()*self.scroll_multiplier)%len(titles)
        titles = titles[i:]+titles[:i]
        titles = titles[:35]
        #return {'full_text': source+': '+titles, 'cached_until': self.py3.time_in(self.cache_timeout)}
        return {'full_text': source+': '+titles, 'cached_until':3}
if __name__ == "__main__":
    """
    Run module in test mode.
    """
    from py3status.module_test import module_test
    module_test(Py3status)
