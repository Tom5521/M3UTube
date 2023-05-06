import sys
import re


if len(sys.argv) < 3:
    print("Usage: python youtube_to_m3u.py <input_file> <output_file>")
    sys.exit(1)


with open(sys.argv[1], "r") as file:
    urls = file.readlines()


youtube_urls = []
for url in urls:
    if re.search("(youtube\.com\/watch\?v=|youtu\.be\/)", url):
        youtube_urls.append(url)


m3u_urls = []
for url in youtube_urls:
    url = url.strip()
    if "youtube.com" in url:
        video_id = re.search("(?<=v=)[\w-]+|(?<=be/)[\w-]+", url).group()
        m3u_urls.append(f"http://www.youtube.com/watch?v={video_id}")
    else:
        video_id = url.split("/")[-1]
        m3u_urls.append(f"http://www.youtube.com/watch?v={video_id}")


with open(sys.argv[2], "w") as file:
    file.write("#EXTM3U\n")
    for i, url in enumerate(m3u_urls):
        file.write(f"#EXTINF:{i+1},YouTube\n{url}\n")
