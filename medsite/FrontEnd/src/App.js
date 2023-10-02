import './App.css';
//import Person from './components/Person';
//import persons from './data/persons';
import Persons from './components/Persons';
import cookieconsent from './CookieConsent';

function App() {
  error_var = 'aaa';
  return (
    <div className="App">
      <Persons />
      {cookieconsent}
    </div>
  );
}

export default App;
