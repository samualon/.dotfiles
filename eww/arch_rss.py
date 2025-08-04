#!/usr/bin/env python3
import feedparser
import json

RSS_FEED = "https://archlinux.org/feeds/news/"

feed = feedparser.parse(RSS_FEED)
headlines = [[entry["title"], entry["link"]] for entry in feed.entries[:10]]

print(json.dumps(headlines))
