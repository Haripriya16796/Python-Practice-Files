'''
The threading module uses threads, the multiprocessing module uses processes
the difference is that threads run in the same memory space
while process have separate memory. This makes it a bit harder to share
objects between processes
'''

import threading
import requests

def download_image(url, filename):
    response = requests.get(url)
    with open(filename, "wb") as f:
        f.write(response.content)
    print(f"{filename} downloaded")

image_urls = [
    "https://www.boredart.com/wp-content/uploads/2018/02/DIY-Filled-Balloons-Decoration-Ideas-12.jpg",
    "https://i0.wp.com/notedlist.com/wp-content/uploads/2015/07/balloon-decoration-ideas/20-balloon-decoration-ideas.jpg",
    "https://img.thrfun.com/img/022/445/party_balloon_ideas_x3.jpg"
]

threads = []
for i, url in enumerate(image_urls):
    filename = f"data/image_{i}.jpg"
    thread = threading.Thread(target = download_image, args = (url, filename))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
print('All images downloaded')


