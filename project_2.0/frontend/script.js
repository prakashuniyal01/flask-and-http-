
const API_BASE_URL = 'http://127.0.0.1:8080';
const APT_MENUENDPOINT = {
    MENU: `${API_BASE_URL}/menu`,
    RECOVER: `${API_BASE_URL}/menu/recover`,
};

// Responsive Navbar Toggle
// document.querySelector('.menu-toggle').addEventListener('click', () => {
//     document.querySelector('.nav-links').classList.toggle('nav-active');
// });




// Fetch menu items from the server 
async function fetchMenuItems() {
    const response = await fetch(APT_MENUENDPOINT.MENU);
    const data = await response.json();
    displayMenuItems(data.data);
}

// Add or update menu item
form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const itemId = document.getElementById('item_id').value;
    const name = document.getElementById('name').value;
    const price = document.getElementById('price').value;
    const category = document.getElementById('category').value;
    const description = document.getElementById('description').value;

    const method = itemId ? 'PUT' : 'POST';

    const response = await fetch(APT_MENUENDPOINT.MENU, {
        method: method,
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ item_id: itemId, name, price, category, description })
    });
    const data = await response.json();
    alert(data.message);
    fetchMenuItems();
    form.reset();
    updateButton.style.display = 'none';
});

// Delete a menu item
async function deleteItem(item_id) {
    const response = await fetch(APT_MENUENDPOINT.MENU, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ item_id })
    });
    const data = await response.json();
    alert(data.message);
    fetchMenuItems();
}

// Recover a menu item
async function recoverItem(item_id) {
    const response = await fetch(APT_MENUENDPOINT.RECOVER, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ item_id })
    });
    const data = await response.json();
    alert(data.message);
    fetchMenuItems();
}

// Display menu items in the UI
function displayMenuItems(items) {
    menuItemsContainer.innerHTML = '';
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

// Call fetchMenuItems on page load
document.addEventListener('DOMContentLoaded', fetchMenuItems);



let isAlreadyProcessing = false;

function handleMessage(event) {
    if (isAlreadyProcessing) return; // Prevent further processing if already in process
    isAlreadyProcessing = true;

    // Process your message here
    console.log('Received:', event.data);

    // Simulate processing delay
    setTimeout(() => {
        isAlreadyProcessing = false; // Reset after processing
    }, 1000);
}

window.addEventListener('message', handleMessage);
