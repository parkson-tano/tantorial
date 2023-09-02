import React, { createContext, useContext, useState, useEffect } from 'react';
import { loginUser, registerUser, logoutUser, getCurrentUser } from '../actions/auth';
import axios from 'axios';
import { API_URL } from '../constant'

const AuthContext = createContext();

export const useAuth = () => {
    return useContext(AuthContext);
};

export const AuthProvider = ({ children }) => {
    const [user, setUser] = useState(getCurrentUser());
    const [isAuthenticated, setIsAuthenticated] = useState(false);
    const [userProfile, setUserProfile] = useState(null);

    useEffect(() => {
        if (user) {
            setIsAuthenticated(true);
        } else {
            setIsAuthenticated(false);
        }
    }, [user]);

    useEffect(() => {
        if (user) {
            API_URL.get(`profile/${user?.account_type}profile/?user=${user.user_id}`)
                .then((res) => {
                    console.log(res);
                    setUserProfile(res.data.results[0]);
                })
                .catch((err) => {
                    console.log(err);
                });
        }
    }, [user])

    const login = async (userData) => {
        const data = await loginUser(userData);
        setUser(data);
    };


    const logout = () => {
        logoutUser();
        setUser(null);
        setUserProfile(null);
        setIsAuthenticated(false);
    };

    const checkAuth = () => {
        const user = getCurrentUser();
        setUser(user);
    };

    const value = {
        user,
        isAuthenticated,
        login,
        logout,
        checkAuth,
        userProfile,
    };

    return (
        <AuthContext.Provider value={value}>
            {children}
        </AuthContext.Provider>
    );
};
