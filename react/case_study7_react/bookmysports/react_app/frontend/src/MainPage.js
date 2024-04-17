import React from 'react';
import './css/MainPage.css';

const MainPage = () => {
    return (
        <div>
            <div className="navbar">
                <a href="/login" className="btn">Login</a>
                <a href="api/register/" className="btn">Signup</a>
            </div>
            <div className="container">
                <h1>Welcome to Book My Sports</h1>
                <div className="quote">
                    <b>"Catch every heartbeat of the game. Reserve your seats and witness the magic!"</b>
                </div>
                <div className="btn-container">
                    <a href="/login" className="btn">Get Started to Book Tickets</a>
                </div>
            </div>
        </div>
    );
};

export default MainPage;
