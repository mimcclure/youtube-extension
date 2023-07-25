from flask import Flask, request, jsonify
from pytube import YouTube
import os

app = Flask(__name__)

videoUrl = input()

@app.route('/download', methods=['POST'])
def download_video(videourl, path):
    #video_url = request.json['video_url']
    #return jsonify()
    yt = YouTube(videourl)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
    yt.download(path)

download_video(videoUrl)