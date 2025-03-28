from flask_cors import CORS      
import os
import openai

app = Flask(__name__)
CORS(app)

TMDBURL = "https://api.themoviedb.org/3"

TMDB_API_KEY = os.getenv("TMDB_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY


