import React, { useEffect, useState } from 'react';
import { MantineProvider } from '@mantine/core';
import {
  BrowserRouter as Router,
  Route,
  Routes,
  Navigate,
} from "react-router-dom";
import { Provider } from 'react-redux';
import { Notifications } from '@mantine/notifications';
import MainRoute from './routes/mainroute/MainRoute';
import { AuthProvider } from './context/auth-context';
import TeacherNav from './components/teacherfeed/TeacherNav';

function App() {
  return (
    <AuthProvider>
      <TeacherNav />
      <Router>
        <Routes>
          <Route path="/*" element={<MainRoute />} />
        </Routes>
      </Router>
    </AuthProvider>
  );
}

export default App;
