import React from 'react';
import {createRoot} from 'react-dom/client';
import App from '@sparkle/App';
import 'semantic-ui-css/semantic.min.css';

const container = document.getElementById('app');
const root = createRoot(container!);
root.render(<App />);
