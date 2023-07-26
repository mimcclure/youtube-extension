from flask import Flask, request, jsonify
from pytube import YouTube
import os

app = Flask(__name__)

SAVE_PATH = "C:/"


#to do
    # Use video_url to download the video as MP3/MP4
    # You can utilize the pytube or youtube-dl libraries for downloading the video
    # Implement the logic to download the video and save it to the server
    # Return a JSON response indicating the success/failure of the download
@app.route('/download', methods=['POST'])
def download_video(videourl, path):
    
    videourl = input('Youtube Link: ')
    try:
        #object creation
        yt = YouTube(videourl)
    except:
        #exception handling
        print("Error validating the link.")

    mp4files = yt.filter('mp4')


    dl_vid = yt.get(mp4files[-1].extension, mp4files[-1].resultion)

    try:
        dl_vid.download(SAVE_PATH)
    except:
        print("Error downloading the video.")