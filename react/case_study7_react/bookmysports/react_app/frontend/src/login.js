// static/js/LoginForm.js

import React, { useState } from 'react';

const LoginForm = () => {
    const [formData, setFormData] = useState({
        user_name: '',
        password: ''
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
        // Process the form data (e.g., send it to a server)
        console.log(formData);
    };

    return (
        <div className="login-container">
            <h2>Login</h2>
            <form onSubmit={handleSubmit} className="login-form" autoComplete="off">
                <div className="form-group">
                    <b>User Name:</b>
                    <input
                        type="text"
                        name="user_name"
                        value={formData.user_name}
                        onChange={handleChange}
                        required
                    />
                </div>
                <div className="form-group password-input">
                    <b>Password:</b>
                    <input
                        type="password"
                        name="password"
                        value={formData.password}
                        onChange={handleChange}
                        required
                    />
                </div>
                <button type="submit" className="btn-login">Login</button>
            </form>
            <div className="register-link">
                <b>If you don't have an account? <a href="{% url 'registration' %}">Register Here</a></b>
            </div>
        </div>
    );
};

export default LoginForm;
