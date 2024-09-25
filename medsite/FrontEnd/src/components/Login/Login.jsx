import styles from './Login.module.css';
import GreenRedButton from '../Chemestry/Atoms/Buttons/GreenRedButton/GreenRedButton';

export default function Login() {
  function handleSubmit(event) {
    event.preventDefault();
    console.log('Submit!');
  }

  return (
    <div className={styles['picture']}>
      <div>
        <form className={styles['form-general']} onSubmit={handleSubmit}>
          <div className={styles['labels']}>
            <label htmlFor="email" className={styles['label']}>
              Email
            </label>
            <input className={styles['input']} id="email" type="email" />
            <label htmlFor="password" className={styles['label']}>
              Password
            </label>
            <input className={styles['input']} id="password" type="password" />
          </div>
          <div className={styles['buttons']}>
            <GreenRedButton
              type="submit"
              name={'Submit'}
              color={'green-button'}
              func={handleSubmit}
            />
            <GreenRedButton
              type="button"
              name={'Cansel'}
              color={'red-button'}
              func={handleSubmit}
            />
          </div>
        </form>
      </div>
    </div>
  );
}
