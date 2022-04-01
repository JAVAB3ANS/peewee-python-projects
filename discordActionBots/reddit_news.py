"""
Connects to the Reddit API to get new submissions details and posts
them to a Discord webhook.
"""

import requests
 
# Constants
WEBHOOK_URL = "[INSERT DISCORD WEBHOOK URL]"
 
def main():
    """Start the script."""

    print("Connecting to Reddit...")
    subreddits = ["news", "worldnews", "politics", "technology", "tech", "technews", "entertainment", "environment", "science", "Music", "LetsTalkMusic"]
    for sr in subreddits:
        print("Scraping /r/%s..." % sr)
        get_rising_submissions(sr)

    print("Data received. Sending webhook...")  

def get_rising_submissions(subreddit):
    """ 
    Connects to the Reddit API and queries the top submissions
    from the specified subreddits.
    
    Parameters
    ----------
    subreddit : str
        The name of the subreddit without forward slashes.
    Returns
    -------
    tuple
        A tuple containing a formatted message and an image url. 
    """

    url = f"https://www.reddit.com/r/{subreddit}/top.json?limit=5"
    headers = {"User-Agent": "Reddit Top Posts Checker v1.0"}

    with requests.get(url, headers=headers) as response:

        data = response.json()["data"]["children"]

        # Iterate over all the children.
        for item in data:

            item_data = item["data"]

            # We will collect only the fields we are interested in.
            subreddit = item_data["subreddit"]
            title = item_data["title"]
            permalink = "https://reddit.com" + item_data["permalink"] 
            image_url = item_data["url"]
            description = item_data["selftext"]
            author = item_data["author"]
            upvotes = item_data["ups"]
            downvotes = item_data["downs"]
            numComments = item_data["num_comments"] 
            footer = f"[ /u/{author} ] | [ {upvotes} 👍 ] | [ {downvotes} 👎 ] | [ {numComments} 📃 ]"

            """
            Sends the formatted message to a Discord server.
            """

            payload = {
                "username": "/r/" + subreddit,
                "embeds": [
                    {    
                        "url": permalink,
                        "title": title,
                        "color": 102204,
                        "description": description,
                        "thumbnail": { "url": image_url }, 
                        "footer": { "text": footer }
                    }
                ]
            }

            with requests.post(WEBHOOK_URL, json=payload) as response:
                print(response.status_code)
  
if __name__ == "__main__": 
    main()