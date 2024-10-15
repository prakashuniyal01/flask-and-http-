// Function to handle API requests
async function apiRequest(endpoint, method, data = null) {
    const options = {
        method: method,
        headers: {
            'Content-Type': 'application/json',
        },
    };

    if (data) {
        options.body = JSON.stringify(data);
    }

    const response = await fetch(`http://localhost:8080${endpoint}`, options);
    
    // Check if response is ok (status in range 200-299)
    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }

    return await response.json();
}

// Fetch menu items
async function fetchMenuItems() {
    try {
        const menuItems = await apiRequest('/menu', 'GET');
        console.log(menuItems); 
        const menuList = document.getElementById('menu-list');
        menuList.innerHTML = '';

        // Ensure data is available
        if (menuItems.data) {
            menuItems.data.forEach(item => {
                const li = document.createElement('li');
                li.textContent = `${item[1]} - $${item[2]}`;
                menuList.appendChild(li);
            });
        console.log(menuItems)
        console.log(menuList);
        
        } else {
            console.error('No data available for menu items');
        }
    } catch (error) {
        console.error('Error fetching menu:', error);
    }
}

// Add new menu item
async function addMenuItem(name, price) {
    try {
        const response = await apiRequest('/menu', 'POST', { name: name, price: price });
        console.log(response);  // Log the response to ensure it's correct
        alert('Menu item added successfully!');
        fetchMenuItems();
    } catch (error) {
        console.error('Error adding menu item:', error);
    }
}


// Event listener for form submission
document.getElementById('add-menu-form').addEventListener('submit', async (event) => {
    event.preventDefault();
    const name = event.target.menuName.value;
    const price = parseFloat(event.target.menuPrice.value);

    if (name && !isNaN(price)) { // Ensure name is not empty and price is a valid number
        await addMenuItem(name, price);
    } else {
        alert('Please enter valid name and price');
    }
});

// Initial fetch of menu items when the page loads
fetchMenuItems();
