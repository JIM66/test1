#coding:utf-8

import random
import config
import json
import requests
import logging
import chardet
__author__ = 'Xaxdus'


logger = logging.getLogger('download')


class Html_Downloader(object):

    @classmethod
    def download(self, url):
        count = 0  # 重试次数
        r = ''
        logger.info("downloading url: %s",url)
        try:
            r = requests.get(url=url, headers=config.HEADER, timeout=config.TIMEOUT)
            r.encoding = chardet.detect(r.content)['encoding']
            while count < config.RETRY_TIME:
                if (not r.ok) or len(r.content) < 500:
                    response = requests.get("http://127.0.0.1:%s/?types=0&count=10" % config.API_PORT)
                    if response.ok:
                        content = response.text
                        choose = random.choice(json.loads(content))
                        proxies = {"https": "http://%s:%s" % (choose[0], choose[1])}
                        try:
                            r = requests.get(url=url, headers=config.HEADER, timeout=config.TIMEOUT, proxies=proxies)
                            r.encoding = chardet.detect(r.content)['encoding']
                            count += 1
                        except Exception as e:
                             count += 1
                    else:
                        return None

                else:
                    return r.text

            return None

        except Exception as e:
            while count < config.RETRY_TIME:
                if r == ''or (not r.ok) or len(r.content) < 500:
                    try:
                        response = requests.get("http://127.0.0.1:%s/?types=0&count=10" % config.API_PORT)
                        if response.ok:
                            content =  response.text
                            choose = random.choice(json.loads(content))
                            proxies={"https": "http://%s:%s" % (choose[0], choose[1])}
                            try:
                                r = requests.get(url=url, headers=config.HEADER, timeout=config.TIMEOUT,
                                                 proxies=proxies)
                                r.encoding = chardet.detect(r.content)['encoding']
                                count += 1
                            except Exception as e:
                                 count += 1
                        else:
                            return None
                    except Exception as e:
                        return None

                else:
                    return r.text

            return None









