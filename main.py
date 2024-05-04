from flask import Flask, render_template, request, redirect, url_for
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stream', methods=['POST', 'GET'])
def stream():
    if request.method == 'POST':
        youtube_url = request.form['youtube_url']
        yt = YouTube(
          youtube_url,
          use_oauth=True,
          allow_oauth_cache=True
        )
        stream = yt.streams.get_highest_resolution()
        stream_url = stream.url

        # Additional video information
        video_title = yt.title
        video_description = yt.description
        video_uploader = yt.author

        return render_template('player.html', stream_url=stream_url, video_title=video_title,
                               video_description=video_description, video_uploader=video_uploader)
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
