import React from 'react';
import { Route, Routes } from 'react-router-dom';

import Header from '../Header/Header';
import MainMenu from '../Header/MainMenu';
import Main from '../Main/Main';
import Article from '../Article/Article';
import ListOfArticles from '../ListOfArticles/ListOfArticles';
import Login from '../Login/Login';
import SignUp from '../SignUp/SignUp';
import Training from '../training/training';

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
        <Route path="/login" element={<Login />} />
        <Route path="/sign-up" element={<SignUp />} />
        <Route path="training" element={<Training />} />
      </Routes>
    </div>
  );
}
