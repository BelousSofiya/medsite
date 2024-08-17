// import { Link } from 'react-router-dom';
import styles from './SideMenu.module.css';

export default function SideMenu() {
  const SideMenuItems = [
    {
      title: 'Your profile',
      link: '1',
    },
    {
      title: 'Your ankets',
      link: '2',
    },
    {
      title: 'Your plans',
      link: '3',
    },
  ];
  const renderItems = (item) => {
    return (
      <div key={item.link} className={styles['side-menu-item']}>
        {item.title}
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
