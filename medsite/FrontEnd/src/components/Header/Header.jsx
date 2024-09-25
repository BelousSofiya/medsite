import { Link } from 'react-router-dom';
import styles from './Header.module.css';

export default function Header() {
  return (
    <div className={styles['main-header']}>
      <div className={styles['logo']}>MEDsite</div>
      <nav className={styles['log-reg-buttons']}>
        <Link to={'/login'} className={styles['link']}>
          login
        </Link>
        <Link to={'/sign-up'} className={styles['link']}>
          register
        </Link>
      </nav>
    </div>
  );
}
