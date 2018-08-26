#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
from telegram_bot import TelegramBot
from settings import TINYRSS


class TinyRSS:
    def __init__(self):
        self.url = TINYRSS.get('url')
        self.user = TINYRSS.get('user')
        self.pwd = TINYRSS.get('password')
        self.feed_ids = TINYRSS.get('feeds')

        self.matching_articles = []

        self._session = requests.Session()
        self.http_auth = ()
        self.sid = self._login()

    # ############### #
    # Private methods #
    # ############### #

    def _get_headlines(self):
        """
        loop through all requested feeds and check for new unread news.
        :return:
        """
        for feed_id in self.feed_ids:
            data = {'sid': self.sid, 'op': 'getHeadlines', 'feed_id': feed_id.get('id'), 'view_mode': 'unread'}
            content = self._post(data)
            tmp = []
            for article in content:
                a = {}
                a['title'] = article.get('title', '')
                a['link'] = article.get('link', '')
                a['source'] = article.get('feed_title', '')
                a['tags'] = article.get('tags', [])
                a['id'] = article.get('id', '')
                a['guid'] = article.get('guid', '')
                tmp.append(a)
            self.matching_articles.append({'label': feed_id, 'articles': tmp})

    def _send_telegram(self):
        """
        send one telegram message per news.
        :return:
        """
        bot = TelegramBot()
        for i in range(0, len(self.matching_articles)):
            current = self.matching_articles[i]
            label = current.get('label').get('name')
            articles = current.get('articles')
            for article in articles:
                try:
                    msg = "\n" \
                          "*New News Item for* {}: \n" \
                          "*Title*: {} \n" \
                          "*Tags*: {} \n" \
                          "*Source*: {} \n" \
                          "*URL*: {} \n".format(label,
                                                article.get('title'),
                                                article.get('tags'),
                                                article.get('source'),
                                                article.get('link'))
                except UnicodeEncodeError as e:
                    msg = "\n" \
                          "*New News Item for* {}: \n" \
                          "*Title*: {} \n" \
                          "*Tags*: {} \n" \
                          "*Source*: {} \n".format(label,
                                                   article.get('title'),
                                                   article.get('tags'),
                                                   article.get('source'))
                bot.send_message(msg)

    def _update_article(self):
        """
        mark all news send to telegram bot as read in TinyRSS instance.
        :return:
        """
        for i in range(0, len(self.matching_articles)):
            current = self.matching_articles[i]
            articles = current.get('articles')
            for article in articles:
                data = {
                    'sid': self.sid,
                    "op": "updateArticle",
                    'article_ids': article.get('id'),
                    'mode': 0,
                    'field': 2
                }
                content = self._post(data)

    # ############## #
    # Helper methods #
    # ############## #

    def _login(self):
        data = {
            "user": self.user,
            "password": self.pwd,
            "op": "login"
        }

        res = self._session.post(self.url, data=json.dumps(data)).json()
        return res.get('content', {}).get('session_id', '')

    def _check_response(self, res):
        try:
            if res.get('content', '').get('error', '') == 'NOT_LOGGED_IN':
                self._login()
                return True
            else:
                return False
        except AttributeError as e:
            return False

    def _post(self, data):
        error = True
        res = None
        while error:
            res = self._session.post(self.url, data=json.dumps(data)).json()
            error = self._check_response(res)
        return res.get('content')

    # ############ #
    # Main methods #
    # ############ #

    def main(self):
        self._get_headlines()
        self._send_telegram()
        self._update_article()


if __name__ == '__main__':
    tiny = TinyRSS()
    tiny.main()
