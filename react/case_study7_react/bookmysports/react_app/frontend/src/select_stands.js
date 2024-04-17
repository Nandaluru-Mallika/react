import React, { useState } from 'react';

function SelectStands({ match, stands, error_message }) {
    const [selectedTickets, setSelectedTickets] = useState({});

    const handleChange = (e) => {
        setSelectedTickets({
            ...selectedTickets,
            [e.target.name]: parseInt(e.target.value, 10),
        });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        // Process the selected tickets (selectedTickets) here
        console.log(selectedTickets);
    };

    return (
        <div className="container">
            <h1>Select Stands and Number of Tickets</h1>
            {error_message && <p style={{ color: 'red' }}>{error_message}</p>}
            <form id="checkoutForm" onSubmit={handleSubmit}>
                <input type="hidden" name="match_id" value={match.id} />
                <ul>
                    {stands.map((stand) => (
                        <li key={stand.name}>
                            <label>
                                <strong>Stand {stand.name}</strong> - Rate: ₹{stand.rate} - Available Tickets: {stand.available_tickets}
                            </label>
                            <input
                                type="number"
                                name={`tickets_${stand.name}`}
                                min="0"
                                max={stand.available_tickets}
                                value={selectedTickets[stand.name] || 0}
                                onChange={handleChange}
                            />
                        </li>
                    ))}
                </ul>
                <button type="submit">Checkout</button>
            </form>
        </div>
    );
}

export default SelectStands;
