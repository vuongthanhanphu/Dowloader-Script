# In[1]: Import Library
import requests
import m3u8
import subprocess

# In[2]:
url = "https://hd.hdbophim.com/20220225/158_4072dce1/1000k/hls/mixed.m3u8" #url of video with m3u8 format
r = requests.get(url)
#print(r.text)

playlist = m3u8.loads(r.text)
#playlist.data['segments'][0]['uri']

#r = requests.get("https://hd.hdbophim.com/20220225/158_4072dce1/1000k/hls/" + playlist.data['segments'][0]['uri'])

with open("Song Song.ts", 'wb') as f:
    for segment in playlist.data['segments']:
        try:
            url = "https://hd.hdbophim.com/20220225/158_4072dce1/1000k/hls/" + segment['uri']
            r = requests.get(url)
            f.write(r.content)
        except Exception as e:
            print("Wrong" + url)
            continue

#subprocess.run(['ffmpeg', '-i', 'vidl.ts', 'vidl.mp4'])
# %%
