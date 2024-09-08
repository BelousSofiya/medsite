import styles from './Articles.module.css';

export default function Article() {
  const ArticleExample = {
    title: 'ArticleExample',
    authors: ['author1', 'author2'],
    date: '20.07.2005',
    source: 'https://www.news-medical.net',
    tags: ['tag1', 'tag2', 'tag3'],
    text:
      'The fundamental idea of industrial microbiology is dependent on the identification of microbes from natural sources ' +
      'for application in large-scale fermentative processes to produce metabolites of industrial interest.2Typically, the isolated ' +
      'microbes are screened and characterized per specific selection criteria. The culture conditions, such as pH, temperature, ' +
      'nutrients, and oxygen levels, are optimized for increased production of the bioproducts.Over the years, the advent and ' +
      'advancements in multiple scientific technologies have revolutionized the field of industrial microbiology. Some of the key ' +
      'areas are discussed below:' +
      'The fundamental idea of industrial microbiology is dependent on the identification of microbes from natural sources ' +
      'for application in large-scale fermentative processes to produce metabolites of industrial interest.2Typically, the isolated ' +
      'microbes are screened and characterized per specific selection criteria. The culture conditions, such as pH, temperature, ' +
      'nutrients, and oxygen levels, are optimized for increased production of the bioproducts.Over the years, the advent and ' +
      'advancements in multiple scientific technologies have revolutionized the field of industrial microbiology. Some of the key ' +
      'areas are discussed below:',
  };

  return (
    <div>
      <div>
        <div>
          <div className={styles['picture']}></div>
        </div>
        <div className={styles['title-info']}>
          <div>Title: {ArticleExample.title}</div>
          <div>Authors: {ArticleExample.authors.join(', ')}</div>
          <div>Date of publishing: {ArticleExample.date}</div>
          <div>Source: {ArticleExample.source}</div>
          <div>Tags: {ArticleExample.tags.join(', ')}</div>
        </div>
      </div>
      <div className={styles['text']}>Text: {ArticleExample.text}</div>
    </div>
  );
}
