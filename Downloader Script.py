# In[1]: Import Library
import requests
import m3u8
import subprocess

# In[2]:
url = "https://hls.streamcdn.xyz/m3u8/57a0c117-cd8d-540d-9ac7-c8fb006fc145"
r = requests.get(url)

m3u8 = m3u8.loads(r.text)

#r = requests.get(m3u8.data['segments'][0]['uri'])
# %%
