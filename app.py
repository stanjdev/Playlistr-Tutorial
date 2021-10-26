from pymongo import MongoClient

client = MongoClient()
db = client.Playlister
playlists = db.playlists

from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

def video_url_creator(id_list):
  videos = []
  for vid_id in id_list:
    video = 'https://youtube.com/embed/' + vid_id
    videos.append(video)
  return videos


# @app.route('/')
# def index():
#   return render_template('home.html', msg='Flask is cool!!')

# playlists = [
#   { 'title': 'Cat Videos', 'description': 'Cats acting weird' },
#   { 'title': '80\'s Music', 'description': 'Don\'t stop believing!' },
#   { 'title': 'MC Hammer', 'description': 'Hammer Time!' }
# ]

@app.route('/')
def playlists_index():
  """ Show all playlists """
  return render_template('playlists_index.html', playlists=playlists.find())

@app.route('/playlists/new')
def playlists_new():
  """ Create a new playlist """
  return render_template('playlists_new.html')

@app.route('/playlists', methods=['POST'])
def playlists_submit():
  """ Submit a new playlist """
  # Grab the video IDs and make a list from them
  video_ids = request.form.get('video_ids').split()
  # call our helper function to create the list of links
  videos = video_url_creator(video_ids)
  playlist = {
    'title': request.form.get('title'),
    'description': request.form.get('description'),
    'videos': videos,
    'video_ids': video_ids
  }
  playlists.insert_one(playlist)
  return redirect(url_for('playlists_index'))






if __name__ == '__main__':
  app.run(debug=True)

