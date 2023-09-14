import React from 'react'
import { Route, Routes } from "react-router-dom";
import AuthWelcome from '../../pages/auth/AuthWelcome';
import StudentRegister from '../../pages/auth/StudentRegister';
import Login from '../../pages/auth/Login';
import TeacherRegister from '../../pages/auth/TeacherRegister';
import ParentRegister from '../../pages/auth/ParentRegister';
import SchoolRegister from '../../pages/auth/SchoolRegister';
import { ForgotPassword } from '../../pages/auth/ForgotPassword';
import TeacherHome from '../../pages/teacher/TeacherHome';

function MainRoute() {
  return (
    <Routes>
      <Route path="/" element={<TeacherHome />} />
      <Route path="/signup-lander" element={<AuthWelcome />} />
      <Route path="/student-register" element={<StudentRegister />} />
      <Route path="/teacher-register" element={<TeacherRegister />} />
      <Route path="/parent-register" element={<ParentRegister />} />
      <Route path="/school-register" element={<SchoolRegister />} />
      <Route path="/forgot-password" element={<ForgotPassword />} />
      <Route path="/login" element={<Login />} />
    </Routes>
  )
}

export default MainRoute