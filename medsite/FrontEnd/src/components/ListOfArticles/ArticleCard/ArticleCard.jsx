import { Link } from 'react-router-dom';

import styles from './ArticleCard.module.css';

export default function ArticleCard({ article }) {
  return (
    <div className={styles['article-card']}>
      <Link
        className={styles['article-card__link']}
        to={`/article/${article.id}`}
      >
        <div className={styles['content']}>
          <div className={styles['article-title']}>{article.title}</div>
          <div className={styles['article-text']}>
            {article.text.slice(0, 100)}{' '}
          </div>
          <div className={styles['article-tags']}>
            {article.tags.join(', ')}
          </div>
        </div>
      </Link>
    </div>
  );
}
