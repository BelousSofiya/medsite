import React from 'react';
import { Route, Routes } from 'react-router-dom';

import Header from '../Header/Header';
import MainMenu from '../Header/MainMenu';
import Main from '../Main/Main';
import Article from '../Article/Article';
import ListOfArticles from '../ListOfArticles/ListOfArticles';

export default function Basic() {
  return (
    <div>
      <div>
        <Header />
        <MainMenu />
      </div>
      <Routes>
        <Route path="/" element={<Main />} />
        <Route path="/article/:id" element={<Article />} />
        <Route path="/articles" element={<ListOfArticles />} />
      </Routes>
    </div>
  );
}
