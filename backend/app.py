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

openai.api_key = OPENAI_API_KEY

def get_movie_from_chatgpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages= [
            {
                "role": "movie suggester",
                "content": "You will provide a Moive suggestion based on the user '{prompt}'. You will need to provide only the title movie and 1 sentence why you chose that movie."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=20,
        temperature=0.3
    )
    return response.choices[0].message['content'].strip()
