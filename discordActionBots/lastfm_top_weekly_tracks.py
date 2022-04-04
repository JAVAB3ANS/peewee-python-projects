# -*- coding: utf-8 -*-
from discord_webhook import DiscordWebhook, DiscordEmbed
import json
import requests  

webhook = DiscordWebhook(url="[insert webhook url]", username="Last.FM")
   
def getTracks(apiKey, user):
    weekly_tracks = requests.get(f"http://ws.audioscrobbler.com/2.0/?method=user.getweeklytrackchart&user={user}&api_key={apiKey}&format=json")
    return json.loads(weekly_tracks.content)

def main():
	# Put here API keys:
    lastFM_user = "[lastfm username]"  # Your Last.fm user
    lastFM_apiKey = "[last.fm api key]" # Last.fm API key

    tracks_embed = DiscordEmbed(color=102204)
    tracks_embed.set_author(name=f"Top weekly tracks for {lastFM_user}")
    tracks_embed.set_footer(text=f"{lastFM_user}'s Daily Picks")
    tracks_embed.set_timestamp()
 
    tracks = getTracks(lastFM_apiKey, lastFM_user) 
    track_data = tracks["weeklytrackchart"]["track"]

    tracks_array = []

    for track_info in track_data[:10]:  
        tracks_array.append(f"{track_info['@attr']['rank']}. [{track_info['name']}]({track_info['url']}) ({track_info['playcount']} plays)")   
    
    tracks_array = "\n".join(tracks_array)
        
    tracks_embed.set_description(tracks_array)

    # add embed object to webhook
    webhook.add_embed(tracks_embed)
    webhook.execute()  

if __name__ == "__main__":
    main()