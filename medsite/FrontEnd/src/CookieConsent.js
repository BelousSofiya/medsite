import CookieConsent from 'react-cookie-consent';
// import boxcookies.png

const cookieconsent = (
  <CookieConsent
    style={{ background: '#1F9A7C' }}
    enableDeclineButton
    buttonText="Погоджуюсь"
    declineButtonText="Відмовляюсь"
    buttonStyle={{
      color: '#1F9A7C',
      background: '#FFFFFF',
      fontSize: '15px',
      borderRadius: '4px',
    }}
    declineButtonStyle={{
      color: '#FFFFFF',
      background: '#FA7979',
      fontSize: '15px',
      borderRadius: '4px',
    }}
    children={<image src="cookieimg/boxcookies.png" />}
    expires={0}
  >
    Наш веб-сайт використовує файли cookie, щоб покращити ваш досвід. Ви можете
    відмовитися, якщо хочете. Дізнатися більше{' '}
    <a href="/privacy">про кукі-файли</a>
  </CookieConsent>
);

export default cookieconsent;
