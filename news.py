import time
from plyer import notification
import requests
import feedparser

# Parse the RSS feed
rss_url1 = 'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml'  # replace with your preferred RSS feed
feed1 = feedparser.parse(rss_url1)

rss_url2 = 'http://feeds.bbci.co.uk/news/rss.xml'
feed2 = feedparser.parse(rss_url2)

# Get the latest news item
if len(feed1.entries) > 0:
 latest_item1 = feed1.entries[0]
 title1 = latest_item1.title
 summary1 = latest_item1.summary

else:
 print ("Error: The RSS feed is empty or invalid.")

if len(feed2.entries) > 0:
 latest_item2 = feed2.entries[0]
 title2 = latest_item2.title
 summary2 = latest_item2.summary

else:
 print ("Error: The RSS feed is empty or invalid.")

def notify_news():
    # Display the notification
    notification_title = 'Latest News: ' + title1[:47] + '...'
    notification_message = summary1
    notification.timeout = 5  # notification will disappear after 10 seconds
    notification.notify(title=notification_title, message=notification_message)
    with open('file.txt', 'r') as f:
            line_count = sum(1 for line in f)
    with open('file.txt', 'a') as f:
        f.write(f"{line_count + 1},Latest News,{title1[:20]},News,NYTimes,High\n")

    
    notification_title = 'Latest News: ' + title2[:47] + '...'
    notification_message = summary2
    notification.timeout = 5  # notification will disappear after 10 seconds
    notification.notify(title=notification_title, message=notification_message)
    with open('file.txt', 'r') as f:
            line_count = sum(1 for line in f)
    with open('file.txt', 'a') as f:
        f.write(f"{line_count + 1},Latest News,{title1[:20]},News,BCCI,High\n")

#notify_news()
