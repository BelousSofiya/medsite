// import { Link } from 'react-router-dom';
import styles from './Header.module.css';

export default function Header() {
  return (
    <div className={styles['main-header']}>
      <div className={styles['med-site']}>MEDsite</div>
      <div className={styles['log-reg-buttons']}>
        <div className={styles['button']}>login</div>
        <div className={styles['button']}>register</div>
      </div>
    </div>
  );
}
