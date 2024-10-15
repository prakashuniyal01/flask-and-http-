const API_BASE_URL = 'http://127.0.0.1:8080';
const API_ENDPOINTS = {
    MENU: `${API_BASE_URL}/menu`,
    RECOVER: `${API_BASE_URL}/menu/recover`,
};

// Helper function to check if response is valid JSON
// Helper function to check if response is valid JSON
async function tryParseJSON(response) {
    const text = await response.text();  // Get the body of the response as text
    try {
        return JSON.parse(text);  // Try to parse the text body as JSON
    } catch (err) {
        throw new Error('Response is not valid JSON: ' + text);
    }
}





// // Fetch menu items from the server
// async function fetchMenu() {
//     try {
//         const response = await fetch(API_ENDPOINTS.MENU, {
//             method: 'GET',
//             headers: {
//                 'Content-Type': 'application/json',
//             }
//         });

//         if (!response.ok) {
//             const errorMessage = await response.text();
//             throw new Error(`Network response was not ok: ${errorMessage}`);
//         }

//         const data = await tryParseJSON(response); // third step
//         displayMenuItems(data.data);  // Access the 'data' field from the response
//     } catch (error) {
//         console.error('Fetch error:', error);
//     }
// }

// Fetch menu items from the server
async function fetchMenu() {
    try {
        const response = await fetch(API_ENDPOINTS.MENU, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            }
        });

        // Log the entire response object for debugging purposes
        console.log('Response:', response);

        if (!response.ok) {
            const errorMessage = await response.text();
            throw new Error(`Network response was not ok: ${errorMessage}`);
        }

        const data = await tryParseJSON(response);  // Correctly parse the response
        displayMenuItems(data.data);  // Use the 'data' field from the response
    } catch (error) {
        console.error('Fetch error:', error);
    }
}

// Add or update menu item
document.getElementById('menu-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const itemId = document.getElementById('item_id').value;
    const name = document.getElementById('name').value;
    const price = parseFloat(document.getElementById('price').value);
    const category = document.getElementById('category').value;
    const description = document.getElementById('description').value;

    if (isNaN(price)) {
        alert("Please enter a valid price.");
        return;
    }

    const method = itemId ? 'PUT' : 'POST';

    try {
        const response = await fetch(API_ENDPOINTS.MENU, {
            method: method,
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ item_id: itemId, name, price, category, description })
        });

        if (!response.ok) {
            const errorMessage = await response.text();  // error message from server
            throw new Error(`Network response was not ok: ${errorMessage}`);
        }

        const data = await tryParseJSON(response);
        alert(data.message);
        fetchMenu();
        document.getElementById('menu-form').reset();
        document.getElementById('update-button').style.display = 'none';
    } catch (error) {
        console.error('Error:', error);
        alert(error.message);
    }
});

// Display menu items in the UI
function displayMenuItems(items) {
    const menuItemsContainer = document.getElementById('menu-items');
    menuItemsContainer.innerHTML = ''; // Clear existing items

    items.forEach(item => {
        const div = document.createElement('div');
        div.classList.add('menu-item');
        div.innerHTML = `
            <h3>${item.name}</h3>
            <p>Price: $${item.price.toFixed(2)}</p>
            <p>Category: ${item.category}</p>
            <p>${item.description}</p>
            <button onclick="prepareUpdate(${item.item_id}, '${item.name}', ${item.price}, '${item.category}', '${item.description}')">Update</button>
            <button onclick="deleteItem(${item.item_id})">Delete</button>
            <button onclick="recoverItem(${item.item_id})" style="display:${item.deleted ? 'block' : 'none'};">Recover</button>
        `;
        menuItemsContainer.appendChild(div);
    });
}

// Prepare for update
function prepareUpdate(itemId, name, price, category, description) {
    document.getElementById('item_id').value = itemId;
    document.getElementById('name').value = name;
    document.getElementById('price').value = price;
    document.getElementById('category').value = category;
    document.getElementById('description').value = description;
    document.getElementById('update-button').style.display = 'inline';
}

// Handle delete and recover actions
async function handleItemAction(action, item_id) {
    const endpoint = action === 'delete' ? API_ENDPOINTS.MENU : API_ENDPOINTS.RECOVER;
    const method = action === 'delete' ? 'DELETE' : 'POST';

    try {
        const response = await fetch(endpoint, {
            method: method,
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ item_id })
        });

        if (!response.ok) {
            const errorMessage = await response.text();
            throw new Error(`Action failed: ${errorMessage}`);
        }

        const data = await tryParseJSON(response);
        alert(data.message);
        fetchMenu();
    } catch (error) {
        console.error('Error:', error);
        alert(error.message);
    }
}

function deleteItem(item_id) {
    handleItemAction('delete', item_id);
}

function recoverItem(item_id) {
    handleItemAction('recover', item_id);
}

// Call fetchMenu on page load
document.addEventListener('DOMContentLoaded', fetchMenu);
