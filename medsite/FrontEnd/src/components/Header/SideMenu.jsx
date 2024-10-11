// import { Link } from 'react-router-dom';
import styles from './SideMenu.module.css';
import { useTranslation } from 'react-i18next';

export default function SideMenu() {
  const { t } = useTranslation();

  const SideMenuItems = [
    {
      title: 'profile',
      link: '1',
    },
    {
      title: 'ankets',
      link: '2',
    },
    {
      title: 'plans',
      link: '3',
    },
  ];
  const renderItems = (item) => {
    return (
      <div key={item.link} className={styles['side-menu-item']}>
        {t(item.title)}
        {/* {item.title} */}
      </div>
    );
  };

  return (
    <div className={styles['side-menu']}>
      <div className={styles['side-menu-items-block']}>
        {SideMenuItems.map(renderItems)}
      </div>
    </div>
  );
}
