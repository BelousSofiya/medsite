import styles from './Login.module.css';
import GreenRedButton from '../Chemestry/Atoms/Buttons/GreenRedButton/GreenRedButton';
import { useTranslation } from 'react-i18next';

export default function Login() {
  function handleSubmit(event) {
    event.preventDefault();
    console.log('Submit!');
  }
  const { t } = useTranslation();

  return (
    <div className={styles['picture']}>
      <div>
        <form className={styles['form-general']} onSubmit={handleSubmit}>
          <div className={styles['labels']}>
            <label htmlFor="email" className={styles['label']}>
              {t('Email')}
            </label>
            <input className={styles['input']} id="email" type="email" />
            <label htmlFor="password" className={styles['label']}>
              {t('Password')}
            </label>
            <input className={styles['input']} id="password" type="password" />
          </div>
          <div className={styles['buttons']}>
            <GreenRedButton
              type="submit"
              name={t('Submit')}
              color={'green-button'}
              func={handleSubmit}
            />
            <GreenRedButton
              type="button"
              name={t('Cansel')}
              color={'red-button'}
              func={handleSubmit}
            />
          </div>
        </form>
      </div>
    </div>
  );
}
