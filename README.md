# M3UTube

# Documentation

This script converts a list of YouTube URLs in a txt file to a remote M3U playlist file that can be read by any music player. The output M3U playlist includes only the valid YouTube URLs found in the input file.
Usage
```
python youtube_to_m3u.py <input_file> <output_file>
```
`input_file`: The name of the input txt file containing the list of YouTube URLs.

`utput_file`: The name of the output M3U playlist file.

## Dependencies

This script requires the Python re module.
Output Format

The output M3U playlist file is formatted according to the M3U file format. Each YouTube URL is preceded by an #EXTINF tag, which specifies the duration of the video (in seconds) and the title of the video (which is set to "YouTube" in this script).
