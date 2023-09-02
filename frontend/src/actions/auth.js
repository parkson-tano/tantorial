import axios from 'axios'
import jwt_decode from 'jwt-decode';
import { useNavigate } from 'react-router-dom';
import { API_URL, URL } from '../constant';

export const loginUser = async (userData) => {
    try {
        const res = await API_URL.post(`auth/login`, userData);
        const token = res.data.access;
        localStorage.setItem('jwtToken', token);
        const decoded = jwt_decode(token);
        return decoded;

    } catch (err) {
        console.log(err);
        throw new Error(err.response ? err.response.data.detail : err.message); // throw an error with the message received from the server
    }
}

export const registerUser = async (userData) => {
    try {
        const res = await axios.post(`${URL}auth/register`, userData);
        return res.data;
    } catch (err) {
        console.log(err);
        throw new Error(err.response ? err.response.data.email : err.message);
    }
}


export const updateUserProfile = async (user, profileData) => {
    try {
        // Fetch the user's profile using a GET request
        const profileResponse = await API_URL.get(`profile/${user.account_type}profile/`);

        // Check if the profileResponse contains valid data and has the 'id' property
        const profiles = profileResponse?.data?.results;
        if (!Array.isArray(profiles) || profiles.length === 0 || !profiles[0].id) {
            throw new Error('Profile data or profile ID not found');
        }

        const profileId = profiles[0].id;

        // Update the user's profile using a PATCH request
        const updateResponse = await API_URL.patch(`profile/${user.account_type}profile/${profileId}/`, profileData);

        return updateResponse.data; // Return the updated profile data
    } catch (err) {
        console.error(err);
        throw new Error(err.response?.data?.message || err.message);
    }
};


export const logoutUser = () => {
    localStorage.removeItem('jwtToken');
}

export const getCurrentUser = () => {
    const token = localStorage.getItem('jwtToken');
    if (token) {
        const decoded = jwt_decode(token);
        return decoded;
    }
    return null;
}

export const apiRequest = axios.create({
    baseURL: API_URL,
    headers: {
        Authorization: `Bearer ${localStorage.jwtToken}`
    }
});