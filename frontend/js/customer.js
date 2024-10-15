// Common API request function
async function apiRequest(endpoint, method = 'GET', body = null) {
    const headers = { 'Content-Type': 'application/json' };
    let options = { method, headers };

    if (body) {
        options.body = JSON.stringify(body);
    }

    try {
        const response = await fetch(`http://localhost:8080${endpoint}`, options);

        // Check for response status and handle errors
        if (!response.ok) {
            const errorData = await response.json(); // Get the error message if any
            throw new Error(errorData.message || 'Something went wrong');
        }

        return await response.json(); // Parse the response data as JSON
    } catch (error) {
        console.error('API Request Failed:', error);
        throw error; // Rethrow error for further handling if needed
    }
}


// Add new customer
async function addCustomer(name, phone_number) {
    try {
        const response = await apiRequest('/customers', 'POST', { name, phone_number });
        alert(response.message);
        await fetchCustomers();  // Call to fetch customers after adding a new one
    } catch (error) {
        console.error('Error adding customer:', error);
    }
}


// Fetch customers
async function fetchCustomers() {
    try {
        const response = await apiRequest('/customers', 'GET');
        const customerList = document.getElementById('customer-list');
        customerList.innerHTML = ''; // Clear existing customer list

        response.data.forEach(customer => { // Assuming the response has a 'data' field containing customer details
            const li = document.createElement('li');
            li.textContent = `${customer[1]} - ${customer[2]}`;
            customerList.appendChild(li);
        });
    } catch (error) {
        console.error('Error fetching customers:', error);
    }
}

// Event listener for form submission
document.getElementById('add-customer-form').addEventListener('submit', async (event) => {
    event.preventDefault(); // Prevent default form submission behavior
    const name = document.getElementById('customerName').value;
    const phone_number = document.getElementById('customerPhoneNumber').value;
    await addCustomer(name, phone_number); // Add the customer
});

// Initial fetch of customers when the script loads
fetchCustomers();
