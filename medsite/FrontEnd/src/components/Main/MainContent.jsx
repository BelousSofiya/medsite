import styles from './MainContent.module.css';
import SideMenu from '../Header/SideMenu';

export default function MainContent() {
  return (
    <div>
      <div className={styles['picture']}>
        <SideMenu />
        <div className={styles['text']}>Welcome to medical hub.</div>
      </div>
    </div>
  );
}
