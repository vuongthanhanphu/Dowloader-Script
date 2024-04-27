# In[1]: Import Library
import requests
import m3u8
import subprocess

# In[2]:
url = "https://vip.opstream17.com/20240320/2896_004a9094/3000k/hls/mixed.m3u8"
r = requests.get(url)
#print(r.text)

playlist = m3u8.loads(r.text)
#playlist.data['segments'][0]['uri']

r = requests.get(playlist.data['segments'][0]['uri'])

with open("video.ts", 'wb') as f:
    for segment in playlist.data['segments']:
        url = segment['uri']
        r = requests.get(url)
        f.write(r.content)

#subprocess.run(['ffmpeg', '-i', 'vidl.ts', 'vidl.mp4'])
# %%
