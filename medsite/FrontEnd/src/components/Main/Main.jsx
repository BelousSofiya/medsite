import Header from '../Header/Header';
import MainMenu from '../Header/MainMenu';
import MainContent from './MainContent';

export default function Main() {
  return (
    <div>
      <Header />
      <MainMenu />
      <div>
        <MainContent />
      </div>
    </div>
  );
}
