# In[1]: Import Library
import requests
import m3u8
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

# In[2]:
# Download movies from source
def download(url, name):
    print("Has come")
    r = requests.get(url)
    print('Loaded url')
    playlist = m3u8.loads(r.text)
    with open(f"{name}.ts", 'wb') as f:
        for segment in playlist.data['segments']:
            try:
                uri = url.replace('mixed.m3u8', '') + segment['uri']
                r = requests.get(uri)
                f.write(r.content)
            except Exception as e:
                print("Wrong " + uri)
                continue

# main
def main():
    
    # Import Movies List
    movieslist = pd.read_excel('MoviesList.xlsx')
    urls = movieslist['url']
    names = movieslist['name']
    
    # Create the thread pool
    with ThreadPoolExecutor() as exe:
        i = 0
        for url in urls:
            exe.submit(download, url, names[i])
            i += 1
    print('Done')
 
# Entry point
if __name__ == '__main__':
    main()

# %%
