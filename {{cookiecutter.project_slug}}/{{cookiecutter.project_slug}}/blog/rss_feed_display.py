#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
rss_feed_display.py

This python script fetches the latest three RSS feed entries
from https://www.techradar.com/rss.

Three entries have been hard-coded, just in case for some reason,
the script fails to fetch the RSS feed

"""
import logging
import re
import traceback
from datetime import datetime

import feedparser
from fake_useragent import UserAgent

# import json     # for testing

# from django.core.serializers.json import DjangoJSONEncoder  # for testing

__author__ = "{{cookiecutter.author_name}}"
__copyright__ = "Copyright {% now 'utc', '%Y' %}, {{ cookiecutter.author_name }}"
__credits__ = [""]
__license__ = "MIT"
__version__ = "{{ cookiecutter.version }}"
__maintainer__ = "{{cookiecutter.author_name}}"
__email__ = "{{cookiecutter.email}}"
__status__ = "Production"

logger = logging.getLogger(__name__)
fmt = "%a, %d %b %Y %H:%M:%S %z"
ua = UserAgent(
    fallback="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2866.71 Safari/537.36"
)  # TODO: this may take a while, need to put it on a task queue

HTTP_STATUS = 200

POSTS = [
    {
        "datetime": datetime.strptime("Fri, 04 Oct 2019 02:30:01 +0000", fmt).date(),
        "description": "It only took a few tweaks here and there, but the Sony Alpha A9 II is shaping up to be one the best pro sports cameras to date.",
        "image": "https://cdn.mos.cms.futurecdn.net/tkgFbQN2MLGiWGoZUZbkbk.jpeg",
        "title": "Sony's electrifying Alpha A9 II full-frame mirrorless just launched out of nowhere",
        "url": "https://www.techradar.com/news/sonys-electrifying-alpha-a9-ii-full-frame-mirrorless-just-launched-out-of-nowhere",
    },
    {
        "datetime": datetime.strptime("Fri, 04 Oct 2019 02:01:53 +0000", fmt).date(),
        "description": "LG’s futuristic Tone+ Free true wireless headphones have a UV light that sanitizes the earbuds when you’re not wearing them.",
        "image": "https://cdn.mos.cms.futurecdn.net/e7XAt9G554upqxqC8ZwmhB.jpg",
        "title": "Sick of cleaning your headphones? These new LG earbuds clean themselves",
        "url": "https://www.techradar.com/news/sick-of-cleaning-your-headphones-these-new-lg-earbuds-clean-themselves",
    },
    {
        "datetime": datetime.strptime("Thu, 03 Oct 2019 23:19:46 +0000", fmt).date(),
        "description": "Amazon Prime offers plenty of benefits for a flat fee. Here’s everything you need to know about the subscription service.",
        "image": "https://cdn.mos.cms.futurecdn.net/jXoeyBMLpDLNTiNzikK45b.jpg",
        "title": "Is Amazon Prime worth it in Australia? Amazon's subscription service explained",
        "url": "https://www.techradar.com/news/amazon-prime-australia",
    },
]


class RSSFetchError(Exception):
    pass


def get_rss_feed_entries():
    """Parses a URL and fetches latest 3 feeds"""
    link = feedparser.parse(
        "https://www.techradar.com/rss",
        request_headers={"User-Agent": ua.random, "Cache-Control": "max-age=0"},
    )

    posts = []

    if link.status == HTTP_STATUS and len(link.entries) != 0:
        for i in range(0, 3):
            # value = str(link["entries"][i])
            # image_url = re.search(
            #     "(?P<url>http?://[^\s]+(png|jpeg|jpg|gif))", value, re.IGNORECASE
            # ).group("url")
            image_url = link["entries"][i].url
            date_only = datetime.strptime(link["entries"][i].published, fmt).date()
            # date_only = link['entries'][i].published    # for testing
            posts.append(
                {
                    "title": link["entries"][i].title,
                    "description": link["entries"][i].summary,
                    "url": (link["entries"][i].link).replace("http://", "https://"),
                    "datetime": date_only,
                    "image": image_url.replace("http://", "https://"),
                }
            )

        return link, posts

    raise RSSFetchError("Failed to Fetch RSS Feed Entries")


def rss_feed_entries():
    """Returns 3 entries whether parsing failed or succeeded"""
    try:
        get_rss_feed_entries()
    except RSSFetchError:
        var = traceback.format_exc()
        logger.error(var)
        return None, POSTS
