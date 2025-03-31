from flask import Flask, request
from flask_cors import CORS      
import os
import openai
import requests

app = Flask(__name__)
CORS(app)

TMDBURL = "https://api.themoviedb.org/3"
TMDB_API_KEY = os.getenv("TMDB_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = openai.Client(api_key=OPENAI_API_KEY)

def get_movie_from_chatgpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"You will provide a Movie suggestion based on the user '{prompt}'. Provide only the movie title and 1 sentence why you chose that movie."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=50,
        temperature=0.3
    )
    return response.choices[0].message.content.strip()

def fetch_tmdb_movie(movie_title):
    url = f"{TMDBURL}/search/movie?api_key={TMDB_API_KEY}&query={movie_title}"
    response = requests.get(url)
    data = response.json()
    results = data.get('results', [])
    if results:
        movie = results[0]
        return {'title': movie['title'], 'overview': movie['overview']}
    return {'title': movie_title, 'overview': 'Not found in TMDB'}

@app.route('/recommend', methods=['POST'])
def recommend_movies():
    prompt = request.json.get('prompt', '')
    chat_response = get_movie_from_chatgpt(prompt)
    try:
        # Split on hyphen and clean quotes from title
        movie_title, reason = chat_response.split(' - ', 1)
        movie_title = movie_title.strip().strip('"')  # Remove quotes
        reason = reason.strip()
    except ValueError:
        movie_title = chat_response
        reason = "No reason provided by ChatGPT."
    movie_details = fetch_tmdb_movie(movie_title)
    movie_details['reason'] = reason
    return movie_details

if __name__ == '__main__':
    app.run(debug=True, port=5001)
