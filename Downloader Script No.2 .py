# In[1]: Import Library
import requests
import m3u8
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
import sys
import time

# In[2]:
# Download movies from source
def download(url, name):
    # Start Timer
    start_time = time.time()
    
    # Get url
    r = requests.get(url)
    print(f'Loaded url {name}')
    playlist = m3u8.loads(r.text)

    # Download
    j = 0
    with open(f"{name}.ts", 'wb') as f:
        for segment in playlist.data['segments']:
            try:
                uri = url.replace('mixed.m3u8', '') + segment['uri']
                r = requests.get(uri)
                f.write(r.content)

                # Downloaded status
                message = f"{name} downloaded: " + str(j) + "/" + str(len(playlist.data['segments']))
                sys.stdout.write("\r" + message)
                sys.stdout.flush()
                j += 1
                
            except Exception as e:
                #print("Wrong " + uri)
                continue
    
    # End Timer
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f" Done {name}: {elapsed_time:.2f} seconds")

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

# Entry point
if __name__ == '__main__':
    main()

# %%
