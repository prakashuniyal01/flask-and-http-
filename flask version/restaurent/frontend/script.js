// Add New Menu Item
document.getElementById('menuForm').addEventListener('submit', function (e) {
    e.preventDefault();

    const name = document.getElementById('name').value;
    const price = document.getElementById('price').value;

    fetch('http://localhost:5000/menu', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name: name, price: price })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        displayMenuItems();  // Refresh menu items list
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

// Add New Customer
document.getElementById('customerForm').addEventListener('submit', function (e) {
    e.preventDefault();

    const name = document.getElementById('customerName').value;
    const phoneNumber = document.getElementById('phoneNumber').value;

    fetch('http://localhost:5000/customers', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name: name, phone_number: phoneNumber })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        displayCustomers();  // Refresh customer list
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

// Place New Order
document.getElementById('orderForm').addEventListener('submit', function (e) {
    e.preventDefault();

    const customerId = document.getElementById('customerId').value;
    const itemId = document.getElementById('itemId').value;
    const quantity = document.getElementById('quantity').value;

    fetch('http://localhost:5000/orders', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ customer_id: customerId, item_id: itemId, quantity: quantity })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

// Fetch and display menu items
function displayMenuItems() {
    fetch('http://localhost:5000/menu')
        .then(response => response.json())
        .then(data => {
            const menuList = document.getElementById('menuList');
            menuList.innerHTML = '';

            data.forEach(item => {
                const li = document.createElement('li');
                li.textContent = `${item.name} - $${item.price}`;
                menuList.appendChild(li);
            });
        })
        .catch(error => {
            console.error('Error fetching menu items:', error);
        });
}

// Fetch and display customers
function displayCustomers() {
    fetch('http://localhost:5000/customers')
        .then(response => response.json())
        .then(data => {
            const customerList = document.getElementById('customerList');
            customerList.innerHTML = '';

            data.forEach(customer => {
                const li = document.createElement('li');
                li.textContent = `ID: ${customer.customer_id}, Name: ${customer.name}, Phone: ${customer.phone_number}`;
                customerList.appendChild(li);
            });
        })
        .catch(error => {
            console.error('Error fetching customers:', error);
        });
}

// Fetch and display order history
// function displayOrderHistory(customerId) {
//     fetch(`http://localhost:5000/orders?customer_id=${customerId}`)
//         .then(response => response.json())
//         .then(data => {
//             const orderList = document.getElementById('orderList');
//             orderList.innerHTML = '';

//             data.forEach(order => {
//                 const li = document.createElement('li');
//                 li.textContent = `Order ID: ${order.order_id}, Item ID: ${order.item_id}, Quantity: ${order.quantity}, Date: ${order.order_date}`;
//                 orderList.appendChild(li);
//             });
//         })
//         .catch(error => {
//             console.error('Error fetching order history:', error);
//         });
// }

// Load data on page load
document.addEventListener('DOMContentLoaded', function () {
    displayMenuItems();
    displayCustomers();
});

// Fetch Order History for a Customer
document.getElementById('orderHistoryForm').addEventListener('submit', function (e) {
    e.preventDefault();

    const customerId = document.getElementById('orderCustomerId').value;
    displayOrderHistory(customerId);  // Call function to fetch order history
});


// Fetch and display order history
function displayOrderHistory(customerId) {
    fetch(`http://localhost:5000/orders?customer_id=${customerId}`)
        .then(response => response.json())
        .then(data => {
            console.log('Order History Data:', data);  // Debugging line
            const orderList = document.getElementById('orderList');
            orderList.innerHTML = '';

            if (data.length === 0) {
                orderList.innerHTML = '<li>No orders found for this customer.</li>';
            } else {
                data.forEach(order => {
                    const li = document.createElement('li');
                    li.textContent = `Order ID: ${order.order_id}, Item ID: ${order.item_id}, Quantity: ${order.quantity}, Date: ${order.order_date}`;
                    orderList.appendChild(li);
                });
            }
        })
        .catch(error => {
            console.error('Error fetching order history:', error);
        });
}
