import styles from './GreenRedButton.module.css';

export default function GreenRedButton({ type, name, color, func }) {
  return (
    <button type={type} className={styles[color]} onClick={func}>
      {name}
    </button>
  );
}
