#!/usr/bin/env python3
import feedparser
import json

RSS_FEED = "https://archlinux.org/feeds/news/"

try:
	feed = feedparser.parse(RSS_FEED)
	headlines = [[entry["title"], entry["link"]] for entry in feed.entries[:10]]
except:
	backup = open("arch_rss_backup.txt", "r")
	headlines = backup.read()

data = json.dumps(headlines)
print(data)

backup = open("arch_rss_backup.txt", "w")
backup.write(data)
backup.close()
