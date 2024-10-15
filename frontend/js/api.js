// // Common API request function
// async function apiRequest(endpoint, method = 'GET', body = null) {
//     const headers = { 'Content-Type': 'application/json' };

//     let options = { method, headers };

//     if (body) {
//         options.body = JSON.stringify(body);
//     }

//     const response = await fetch(`http://localhost:8080${endpoint}`, options);
//     const data = await response.json();

//     if (!response.ok) {
//         throw new Error(data.message || 'Something went wrong');
//     }

//     return data;
// }

// Common API request function
const BASE_URL = 'http://localhost:8080'; // Base URL for the API

async function apiRequest(endpoint, method = 'GET', body = null) {
    const headers = { 'Content-Type': 'application/json' };

    let options = { method, headers };

    if (body) {
        options.body = JSON.stringify(body);
    }

    try {
        const response = await fetch(`${BASE_URL}${endpoint}`, options);
        
        // Check if response is OK
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.message || 'Something went wrong');
        }

        // Attempt to parse response as JSON
        const data = await response.json();
        return data;

    } catch (error) {
        console.error('API Request Failed:', error);
        throw error; // Rethrow error for further handling if needed
    }
}
