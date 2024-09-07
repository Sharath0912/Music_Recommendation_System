from flask import Flask, render_template, request, redirect, url_for
from recommendations import recommend_songs

app = Flask(__name__)

@app.route('/', methods=['GET'])
def input_page():
    return render_template('input.html')

@app.route('/recommendations', methods=['POST'])
def recommendations():
    genre = request.form.get('genre')
    artist = request.form.get('artist')
    recommendations = recommend_songs(genre=genre, artist=artist)
    return render_template('result.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)  # Ensure Flask runs on 0.0.0.0 so it's accessible from Docker
