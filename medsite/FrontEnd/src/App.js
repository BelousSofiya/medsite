import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import Basic from './components/Basic/Basic';

import './App.css';

function App() {
  const router = createBrowserRouter([
    {
      path: '/*',
      element: <Basic />,
    },
  ]);
  return (
    <div>
      <RouterProvider router={router} />
    </div>
  );
}

export default App;
