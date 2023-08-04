import axios from 'axios'
import jwt_decode from 'jwt-decode';
import { useNavigate } from 'react-router-dom';
import { API_URL } from '../constant';

export const loginUser = async (userData) => {
    try {
        const res = await axios.post(`${API_URL}auth/login`, userData);
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
        const res = await axios.post(`${API_URL}auth/register`, userData);
        console.log(res.data);
        // const profileResponse = await axios.get(`${API_URL}profile/${res?.data?.account_type}profileupdate/?user_id=${res?.data?.id}`);
        // const updateResponse = await axios.patch(`${API_URL}profile/${user.account_type}profile/${profileResponse}/`, profileData);
        // console.log(profileResponse);

        return res.data;
    } catch (err) {
        console.log(err);
        throw new Error(err.response ? err.response.data.email : err.message);
    }
}


// export const updateUserProfile = async (user, profileData) => {
//     try {
//         // Fetch the user's profile using a GET request
//         const profileResponse = await axios.get(`${API_URL}profile/${user.account_type}profileupdate/?user_id=${user?.id}`);
//         const profileId = profileResponse.data.id;

//         console.log('Profile ID:', profileId);
//         console.log('Profile data:', profileResponse);

//         // Update the user's profile using a PATCH request
//         const updateResponse = await axios.patch(`${API_URL}profile/${user.account_type}profile/${profileId}/`, profileData);

//         return updateResponse.data; // Return the updated profile data
//     } catch (err) {
//         console.error(err);
//         throw new Error(err.response ? err.response.data.message : err.message);
//     }
// }


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