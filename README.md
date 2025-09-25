# Movie Recommender Application

This is a **full-stack web application** designed to help users find movies more easily by providing AI-powered movie recommendations. The application addresses the common problem of "endless scrolling" on streaming platforms by offering intelligent movie suggestions based on user prompts.

## Architecture Overview

The application follows a **client-server architecture** with:

- **Backend**: Flask (Python) API server
- **Frontend**: React.js web application
- **AI Integration**: OpenAI GPT-3.5-turbo for movie recommendations
- **Movie Database**: The Movie Database (TMDB) API for movie details

## Core Functionality

### How It Works:
1. **User Input**: Users enter a descriptive prompt (e.g., "movie for a family night", "scary horror movie", "romantic comedy")
2. **AI Processing**: The prompt is sent to OpenAI's GPT-3.5-turbo model, which analyzes the request and suggests an appropriate movie title with a brief explanation
3. **Movie Details**: The suggested movie title is then used to fetch detailed information (plot summary, etc.) from TMDB
4. **Results Display**: The application presents the movie title, overview, and AI-generated reasoning for the recommendation

### Key Features:
- **Natural Language Processing**: Users can describe what kind of movie they want in plain English
- **AI-Powered Recommendations**: Uses OpenAI's language model to understand context and suggest relevant movies
- **Rich Movie Information**: Integrates with TMDB to provide comprehensive movie details
- **Theater-Themed UI**: Features a cinema-inspired design with movie theater aesthetics
- **Real-time Processing**: Provides immediate recommendations with loading states

## Technical Implementation

### Backend (Flask API):
- **Framework**: Flask with CORS support for cross-origin requests
- **AI Integration**: OpenAI Python client for GPT-3.5-turbo
- **External APIs**: TMDB API for movie data retrieval
- **Environment Variables**: Secure API key management
- **Error Handling**: Graceful handling of API failures and missing data

### Frontend (React):
- **Framework**: React 18 with functional components and hooks
- **HTTP Client**: Axios for API communication
- **State Management**: React useState for form handling and data display
- **Responsive Design**: Theater-themed CSS with gradient backgrounds and movie aesthetics
- **User Experience**: Loading states, error handling, and intuitive form interactions

### Dependencies:
- **Backend**: Flask, OpenAI, Requests, Flask-CORS, Gunicorn
- **Frontend**: React, Axios, Testing libraries

## User Interface Design

The application features a **cinema-inspired design** with:
- **Theater Background**: Dark gradient with subtle film reel effects
- **Ticket Booth**: Red-themed form area for user input
- **Movie Screen**: White display area for recommendations
- **Golden Accents**: Gold/yellow color scheme reminiscent of classic movie theaters
- **Responsive Layout**: Centered content with maximum width constraints for readability

## Setup and Installation

### Prerequisites:
- Python 3.11+
- Node.js and npm
- TMDB API key
- OpenAI API key

### Backend Setup:
1. Navigate to the backend directory
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Set environment variables:
   - `TMDB_API_KEY`: Your TMDB API key
   - `OPENAI_API_KEY`: Your OpenAI API key
   - `PORT`: Port number (default: 5001)
6. Run the server: `python app.py`

### Frontend Setup:
1. Navigate to the frontend directory
2. Install dependencies: `npm install`
3. Set environment variable:
   - `REACT_APP_API_URL`: Backend API URL (e.g., http://localhost:5001)
4. Run the development server: `npm start`

## Deployment & Configuration

- **Environment Variables**: Requires TMDB_API_KEY and OPENAI_API_KEY
- **Port Configuration**: Backend runs on port 5001 (configurable)
- **Production Ready**: Includes Gunicorn for production deployment
- **Frontend Build**: React build system with Vercel deployment configuration

## Use Cases

This application is perfect for:
- **Decision Fatigue**: When users can't decide what to watch
- **Specific Moods**: Finding movies for particular occasions or moods
- **Discovery**: Discovering new movies based on preferences
- **Family Entertainment**: Finding appropriate content for different audiences
- **Quick Recommendations**: Getting instant suggestions without browsing

## Why This Project?

Built this project to find movies easier, since it's difficult finding movies when there are so many options. I wanted to create something that would help me endless scroll on Netflix, so I created an AI movie recommender. The AI will find a movie based on your prompt.

So hopefully it's a quicker way to find something to watch!

The application essentially acts as an **intelligent movie concierge**, combining the power of AI language understanding with comprehensive movie databases to provide personalized recommendations in a user-friendly, visually appealing interface.

