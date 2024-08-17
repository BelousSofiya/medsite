// import { Link } from 'react-router-dom';
import styles from './HeaderAnt.module.css';

export default function HeaderAnt() {
  const MenuItems = [
    {
      title: 'Articles',
      link: '',
    },
    {
      title: 'Protocols',
      link: '',
    },
    {
      title: 'Organizations',
      link: '',
    },
  ];

  const SiderItems = [
    {
      title: 'Your profile',
      link: '',
    },
    {
      title: 'Some link',
      link: '',
    },
    {
      title: 'Some link',
      link: '',
    },
  ];

  return (
    <div className={styles['main-header']}>
      <div className={styles['']}>
        <div className={styles['logo']}>LOGO</div>
        <div className={styles['menu-items']}>
          {MenuItems.map((element) => (
            <div className={styles['menu-item']} key={element.link}>
              {/* <Link to={element.link}>{element.title}</Link> */}
              {element.title}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
