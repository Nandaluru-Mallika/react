import React, { useState } from 'react';
import { useSelector } from 'react-redux'; // If you're using Redux for state management

function UpcomingMatches() {
    const teams = useSelector(state => state.teams); // Assuming teams are stored in Redux state
    const upcomingMatches = useSelector(state => state.upcomingMatches); // Assuming upcomingMatches are stored in Redux state

    const [selectedTeam, setSelectedTeam] = useState('');

    const handleTeamChange = (e) => {
        setSelectedTeam(e.target.value);
    };

    const filteredMatches = selectedTeam ? upcomingMatches.filter(match => match.team === selectedTeam) : upcomingMatches;

    return (
        <div className="container">
            <h1>Upcoming Matches</h1>
            <div className="team-filter">
                <label htmlFor="team-filter">Select Team:</label>
                <select id="team-filter" value={selectedTeam} onChange={handleTeamChange}>
                    <option value="">All Teams</option>
                    {teams.map(team => (
                        <option key={team.id} value={team.abbreviation}>{team.team_name}</option>
                    ))}
                </select>
                <button type="button">Filter</button>
            </div>
            <div className="matches-container">
                {filteredMatches.length > 0 ? (
                    filteredMatches.map(match => (
                        <div key={match.id} className="match-box">
                            <div className="match-details">
                                <p>{match.match_name}</p>
                                <p>Date: {match.match_date}</p>
                                <p>Time: {match.match_time}</p>
                            </div>
                            <a href={`/book_match/${match.id}`} className="book-button">Book</a>
                        </div>
                    ))
                ) : (
                    <p>No upcoming matches</p>
                )}
            </div>
        </div>
    );
}

export default UpcomingMatches;
