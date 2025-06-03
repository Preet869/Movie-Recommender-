import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [prompt, setPrompt] = useState('');
  const [movie, setMovie] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    setLoading(true);
    try {
      const response = await axios.post(`${process.env.REACT_APP_API_URL}/recommend`, { prompt });
      setMovie(response.data);
    } catch (err) {
      setError('Failed to get recommendation. Is the backend running?');
      console.error(err);
    }
    setLoading(false);
  };

  return (
    <div className="theater">
      <h1>Movie Recommender</h1>
      <div className="ticket-booth">
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            placeholder="e.g., movie for a family night"
          />
          <button type="submit" disabled={loading}>
            {loading ? 'Rolling Film...' : 'Get Ticket'}
          </button>
        </form>
        {error && <p className="error">{error}</p>}
        {loading && <p className="loading">Rolling Film...</p>}
      </div>
      {movie && (
        <div className="screen">
          <h2>{movie.title}</h2>
          <p className="overview">{movie.overview}</p>
          <p className="reason"><em>Why Watch:</em> {movie.reason}</p>
        </div>
      )}
    </div>
  );
}

export default App;