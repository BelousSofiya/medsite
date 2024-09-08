import React from 'react';
import { Route, Routes } from 'react-router-dom';

import Header from '../Header/Header';
import MainMenu from '../Header/MainMenu';
import Main from '../Main/Main';

export default function Basic() {
  return (
    <div>
      <div>
        <Header />
        <MainMenu />
      </div>
      <Routes>
        <Route path="/" element={<Main />} />
      </Routes>
    </div>
  );
}
