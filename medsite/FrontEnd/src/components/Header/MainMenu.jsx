import { Link } from 'react-router-dom';
import styles from './MainMenu.module.css';

export default function MainMenu() {
  const MenuItems = [
    {
      title: 'Articles',
      link: '1',
    },
    {
      title: 'Protocols',
      link: '2',
    },
    {
      title: 'Organizations',
      link: '3',
    },
  ];
  const renderItems = (item) => {
    return (
      <Link
        key={item.link}
        className={styles['menu-item']}
        to={`${item.title.toLowerCase()}`}
      >
        {item.title}
      </Link>
    );
  };

  return (
    <div className={styles['main-menu']}>
      <div className={styles['menu-items-block']}>
        {MenuItems.map(renderItems)}
      </div>
    </div>
  );
}
