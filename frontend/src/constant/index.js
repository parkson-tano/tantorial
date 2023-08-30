import axios from "axios";

export const API_URL = "http://127.0.0.1:8000/";

export const fetchSchools = async (subsystem) => {
    try {
        const response = await axios.get(`${API_URL}profile/schoolprofile/`);
        const res = response.data.results;
        const data = res.map((item) => ({
            value: item.id,
            label: item.school_name,
        }));
        return data; // Return the data array
    } catch (error) {
        throw new Error(error.response ? error.response.data.message : error.message);
    }
};

export const fetchClasses = async () => {
    try {
        const response = await axios.get(`${API_URL}subsystem/classroom/`);
        const res = response.data.results;
        const data = res.map((item) => ({
            value: item.id,
            label: item.title,
        }));
        return data; // Return the data array

    } catch (error) {
        throw new Error(error.response ? error.response.data.message : error.message);
    }
};

export const fetchSubsystems = async () => {
    try {
        const response = await axios.get(`${API_URL}subsystem/subsystem/`);
        const res = await response?.data?.results;
        const data = await res?.map((item) => ({
            value: item.id,
            label: item.title,
        }));
        return data; // Return the data array
    } catch (error) {
        throw new Error(error.response ? error.response.data.message : error.message);
    }
};
