// import { Link } from 'react-router-dom';
import styles from './Header.module.css';

export default function Header() {
  return (
    <div className={styles['main-header']}>
      <div className={styles['logo']}>MEDsite</div>
      <nav className={styles['log-reg-buttons']}>
        <div>login</div>
        <div>register</div>
      </nav>
    </div>
  );
}
