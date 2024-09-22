import styles from './GreenRedButton.module.css';

export default function GreenRedButton({ name, color }) {
  return <button className={styles[color]}>{name}</button>;
}
