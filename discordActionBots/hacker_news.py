import requests
import datetime as dt
import re
import html 

# Constants
WEBHOOK_URL = "[INSERT DISCORD WEBHOOK URL]"
MAX_POSTS = 10
TOP_POSTS_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
GET_ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"
REQUEST_HEADER = {"User-Agent": "Hacker News Top 10 Bot v1.0"}

def clean_text(text):
  """
  Removes HTML tags, unescapes HTML entities, and truncates text to 280 characters.
  Parameters
  ----------
  text : str
    HTML text
  """
  cleaned_text = html.unescape(re.sub(re.compile("<.*?>"), "", text))

  if len(cleaned_text) > 280:
    cleaned_text = f"{cleaned_text[:277]}..."
  
  return cleaned_text

def fetch_top_posts(max_posts):
  """
  Fetches post IDs of top posts via the API
  Parameters
  ----------
  max_posts : int
    Number of post IDs to be returned.
  """
  with requests.get(TOP_POSTS_URL, headers=REQUEST_HEADER) as response:
    item_ids = response.json()
    item_ids = item_ids[:max_posts]
    posts = [get_item(item_id) for item_id in item_ids]

    return posts

def get_item(item_id):
  """
  Fetches post metadata
  Parameters
  ----------
  item_id : int
    The post ID.
  """
  with requests.get(GET_ITEM_URL.format(item_id), headers=REQUEST_HEADER) as response:
    data = response.json()

    item = {}
    item["id"] = data.get("id")
    item["timestamp"] = f"{dt.datetime.fromtimestamp(data.get('time')).strftime('%Y-%m-%dT%H:%M:%S')}.000Z"
    item["by"] = data.get("by")
    item["title"] = data.get("title")
    item["comments"] = data.get("descendants")
    item["score"] = data.get("score")
    item["permalink"] = f"https://news.ycombinator.com/item?id={item['id']}"
    item["url"] = data.get("url")
    item["text"] = data.get("text")

    if item["url"] == None:
      item["url"] = item["permalink"]
    
    if item["text"] == None:
      item["text"] = ""
    else:
      item["text"] = clean_text(item["text"])

    return item

def send_to_webhook(posts):
  """
  Sends the JSON payload to a Discord Webhook URL
  Parameters
  ----------
  posts : list
    A list of posts.
  """
  current_date = dt.date.today().strftime("%B %d, %Y")

  payload = {
    "username": "Hacker News",
    "avatar_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Y_Combinator_logo.svg/240px-Y_Combinator_logo.svg.png",
    "content": f"**Top {MAX_POSTS} Posts from Hacker News ({current_date})**",
    "embeds": [
      {
        "color": "16737792",
        "author": {
          "name": post["by"]
        },
        "title": f"{post['title']}",
        "url": f"{post['url']}",
        "description": "" if post['text'] == None else f"{post['text']}",
        "timestamp": post["timestamp"],
        "fields": [
          {
            "name": "Post ID",
            "value": f"[{post['id']}]({post['permalink']})",
            "inline": True
          },
          {
            "name": "Score",
            "value": f"{post['score']} points",
            "inline": True
          },
          {
            "name": "Comments",
            "value": f"{post['comments']}",
            "inline": True
          }
        ],
        "footer": {
          "text": "Hacker News",
          "icon_url": "https://news.ycombinator.com/y18.gif"
        }
      } for post in posts
    ]
  }

  with requests.post(WEBHOOK_URL, json=payload) as response:
    print(response.status_code)

def main():
  print("Connecting to Hacker News...")
  posts = fetch_top_posts(MAX_POSTS)
  print("Data received. Sending to webhook...")
  send_to_webhook(posts)

if __name__ == "__main__":
  main()