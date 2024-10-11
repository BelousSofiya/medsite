import React from 'react';
import ReactDOM from 'react-dom/client';

import './index.css';
import App from './App';
// import i18n from './utils/i18n';
import './utils/i18n/i18n';

// console.log(i18n.lng);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
