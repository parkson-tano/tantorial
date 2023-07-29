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


function App() {
  return (
    <AuthProvider>
    <Router>
      <Routes>
        <Route path="/*" element={<MainRoute />} />
      </Routes>
    </Router>
    </AuthProvider>
  );
}

export default App;
