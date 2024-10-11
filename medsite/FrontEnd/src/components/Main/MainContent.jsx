import styles from './MainContent.module.css';
import SideMenu from '../Header/SideMenu';
import { useTranslation } from 'react-i18next';
// import i18n from './utils/i18n';

export default function MainContent() {
  const { t } = useTranslation();

  return (
    <div>
      <div className={styles['picture']}>
        <SideMenu />
        <div className={styles['text']}>{t('Welcome')}</div>
      </div>
    </div>
  );
}
