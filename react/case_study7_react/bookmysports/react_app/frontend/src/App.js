import React from 'react';
import { createRoot } from 'react-dom'; // Import createRoot from react-dom
import MainPage from './MainPage'; // Import your MainPage component

// Use createRoot to render your application
createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <MainPage />
  </React.StrictMode>
);

// Export MainPage
export default MainPage;
