import { Link } from 'react-router-dom';
import styles from './Header.module.css';
import { useTranslation } from 'react-i18next';

export default function Header() {
  const { t } = useTranslation();

  return (
    <div className={styles['main-header']}>
      <div className={styles['logo']}>MEDsite</div>
      <nav className={styles['log-reg-buttons']}>
        <Link to={'/login'} className={styles['link']}>
          {t('login')}
        </Link>
        <Link to={'/sign-up'} className={styles['link']}>
          {t('register')}
        </Link>
      </nav>
    </div>
  );
}
