from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/download', methods=['POST'])
def download_video():
    video_url = request.json['video_url']
    return jsonify()