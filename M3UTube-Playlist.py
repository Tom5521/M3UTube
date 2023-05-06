import argparse
import re
import urllib.request
import os

parser = argparse.ArgumentParser(description="Convierte una playlist de YouTube en una lista de links a los videos dentro de un archivo txt")
parser.add_argument("link", help="URL de la playlist de YouTube que deseas convertir")
parser.add_argument("output", help="Nombre del archivo de salida")


args = parser.parse_args()

playlist_id = re.search(r"list=([\w-]+)", args.link).group(1)

url = f"https://www.youtube.com/playlist?list={playlist_id}"


with urllib.request.urlopen(url) as response:
    html = response.read().decode()


regex = r"watch\?v=([A-Za-z0-9_-]{11})"
matches = re.findall(regex, html)


with open(args.output, "w") as f:
    for match in matches:
        video_url = f"https://www.youtube.com/watch?v={match}"
        f.write(video_url + "\n")

os.system(f"python M3UTube.py {args.output} {args.output}.m3u")