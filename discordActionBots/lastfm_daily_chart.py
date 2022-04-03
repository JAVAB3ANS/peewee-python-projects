from discord_webhook import DiscordWebhook, DiscordEmbed
import sys 
import urllib.request
import requests

webhook = DiscordWebhook(url="[INSERT WEBHOOK URL]", username="Last.FM")

PERIODS_MAP = {
  "7 days": "7day",
  "1 month": "1month",
  "3 months": "3month",
  "6 months": "6month",
  "12 months": "12month",
  "overall": "overall"
}

SIZES_MAP = {
  "3x3": "3x3",
  "4x4": "4x4",
  "5x5": "5x5"
} 

username = "[INSERT LAST.FM USERNAME]"  
period = "7 days"
size = "5x5"
captions = True
  
def main(): 
  if period not in PERIODS_MAP.keys() or size not in SIZES_MAP.keys():
    print("`period` and `size` must be a key of their respective maps")
    sys.exit(1)

  print(f"Downloading a {size} chart for user {username}, from the past {period}...") 

  try: 
    final_url = f"https://tapmusic.net/collage.php?user={username}&type={PERIODS_MAP[period]}&size={SIZES_MAP[size]}{'&caption=true' if captions else ''}"

    resp = requests.get(final_url) 

    if resp.status_code == 200:
      
      print(f"[{resp.status_code}] Data received. Sending to webhook...")

      urllib.request.urlretrieve(final_url, "./daily-last-fm-chart/daily-last-fm-chart.jpg")
 
      with open("./daily-last-fm-chart/daily-last-fm-chart.jpg", "rb") as f:
        webhook.add_file(file=f.read(), filename="./daily-last-fm-chart/daily-last-fm-chart.jpg")

      embed = DiscordEmbed(color=102204)
      embed.set_author(name=f"{PERIODS_MAP[period]} Weekly Chart for {username}")
      embed.set_footer(text=f"{username}'s Daily Picks")
      embed.set_timestamp()

      # add embed object to webhook
      webhook.add_embed(embed)
      webhook.execute()

      print("Has been sent!") 
  except Exception as e:
    print("Couldn't download chart!\n[ERROR] ", e)

if __name__ == "__main__":
  main() 
