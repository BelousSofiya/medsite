import styles from './ListOfArticles.module.css';
import ArticleCard from './ArticleCard/ArticleCard';

export default function ListOfArticles() {
  const ArticlesList = [
    {
      id: '1',
      title: 'Article1',
      authors: ['author1', 'author2'],
      date: '20.07.2005',
      source: 'https://www.news-medical.net',
      tags: ['tag1', 'tag2', 'tag3'],
      text: 'iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii',
    },
    {
      id: '2',
      title: 'Article2',
      authors: ['author3', 'author4'],
      date: '20.07.2006',
      source: 'https://www.news-medical.net',
      tags: ['tag4', 'tag5', 'tag6'],
      text: 'wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww',
    },
    {
      id: '3',
      title: 'Article3',
      authors: ['author5', 'author6'],
      date: '20.07.2007',
      source: 'https://www.news-medical.net',
      tags: ['tag7', 'tag8', 'tag9'],
      text: 'qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq',
    },
    {
      id: '4',
      title: 'Article4',
      authors: ['author7', 'author8'],
      date: '20.07.2007',
      source: 'https://www.news-medical.net',
      tags: ['tag10', 'tag11', 'tag12'],
      text: 'vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv',
    },
  ];

  return (
    <div className={styles['background']}>
      <div className={styles['list-container']}>
        {ArticlesList.map((result, resultIndex) => (
          <div key={resultIndex} className={styles['art-list']}>
            <ArticleCard article={result} />
          </div>
        ))}
      </div>
    </div>
  );
}
