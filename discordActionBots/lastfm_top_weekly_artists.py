# -*- coding: utf-8 -*-
from discord_webhook import DiscordWebhook, DiscordEmbed
import json
import requests  

webhook = DiscordWebhook(url="[insert webhook url]", username="Last.FM")
   
def getArtists(apiKey, user):
    weekly_artists = requests.get(f"http://ws.audioscrobbler.com/2.0/?method=user.getweeklyartistchart&user={user}&api_key={apiKey}&format=json")
    return json.loads(weekly_artists.content)

def main():
	# Put here API keys:
    lastFM_user = "[insert last.fm username]" # Your Last.fm user
    lastFM_apiKey = "[insert last.fm api key]" # Last.fm API key

    artists_embed = DiscordEmbed(color=102204)
    artists_embed.set_author(name=f"Top weekly artists for {lastFM_user}")
    artists_embed.set_footer(text=f"{lastFM_user}'s Daily Picks")
    artists_embed.set_timestamp()
 
    artists = getArtists(lastFM_apiKey, lastFM_user) 
    artist_data = artists["weeklyartistchart"]["artist"]

    artists_array = []

    for artist_info in artist_data[:10]:  
        artists_array.append(f"{artist_info['@attr']['rank']}. [{artist_info['name']}]({artist_info['url']}) ({artist_info['playcount']} plays)")   
    
    artists_array = "\n".join(artists_array)
        
    artists_embed.set_description(artists_array)

    # add embed object to webhook
    webhook.add_embed(artists_embed)
    webhook.execute()  

if __name__ == "__main__":
    main()