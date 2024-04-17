import React, { useState } from 'react';

const UserRegistrationForm = () => {
    const [formData, setFormData] = useState({
        user_name: '',
        password: '',
        user_address: '',
        user_mobile: '',
        user_email: ''
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: value
        });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        fetch('/api/register/', {
            method: 'POST',
            body: JSON.stringify(formData),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => {
            if (response.ok) {
                // Redirect to the login page after successful registration
                window.location.href = '/login';
            } else {
                // Handle registration failure
                console.error('Registration failed');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    };

    return (
        <form onSubmit={handleSubmit}>
            <div>
                <label>Your Name:</label>
                <input
                    type="text"
                    name="user_name"
                    value={formData.user_name}
                    onChange={handleChange}
                    required
                />
            </div>
            <div>
                <label>Password:</label>
                <input
                    type="password"
                    name="password"
                    value={formData.password}
                    onChange={handleChange}
                    required
                />
            </div>
            <div>
                <label>Your Address:</label>
                <input
                    type="text"
                    name="user_address"
                    value={formData.user_address}
                    onChange={handleChange}
                    required
                />
            </div>
            <div>
                <label>Phone Number:</label>
                <input
                    type="text"
                    name="user_mobile"
                    value={formData.user_mobile}
                    onChange={handleChange}
                    required
                />
            </div>
            <div>
                <label>Your Email:</label>
                <input
                    type="email"
                    name="user_email"
                    value={formData.user_email}
                    onChange={handleChange}
                    required
                />
            </div>
            <button type="submit">Submit</button>
        </form>
    );
};

export default UserRegistrationForm;
