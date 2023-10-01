import './App.css';
//import Person from './components/Person';
//import persons from './data/persons';
import Persons from './components/Persons'
import cookieconsent from './CookieConsent'
const abra = 'abra'

function App() {
  return (
    <div className="App">
      <Persons />
      {cookieconsent}
    </div>
  );
}

export default App
