// api.js

const API_URL = 'http://localhost:8000'; // Your Django backend URL

// Function to save user data to the backend
export const saveUserData = async (userData) => {
  try {
    const response = await fetch(`${API_URL}/api/register/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(userData),
    });
    if (!response.ok) {
      throw new Error('Failed to save user data');
    }
    return await response.json();
  } catch (error) {
    console.error('Error:', error);
    throw error;
  }
};
