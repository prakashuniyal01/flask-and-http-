// API request function
async function apiRequest(url, method, body = null) {
    try {
        const options = {
            method: method,
            headers: {
                'Content-Type': 'application/json',
            },
        };

        if (body) {
            options.body = JSON.stringify(body);
        }

        const response = await fetch(`http://localhost:8080${url}`, options);
        const responseBody = await response.text(); // Get raw response

        // Log the raw response for debugging purposes
        console.log('Raw response:', responseBody);

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        return JSON.parse(responseBody); // Parse the response after logging
    } catch (error) {
        console.error('API request failed:', error);
        throw error;
    }
}

// Place a new order
async function placeOrder(customerId, itemId, quantity, orderDate) {
    try {
        const orderData = {
            customer_id: customerId,
            item_id: itemId,
            quantity: quantity,
            order_date: orderDate
        };

        await apiRequest('/order', 'POST', orderData);
        alert('Order placed successfully!');
        await fetchOrderHistory(); // Refresh the order history
    } catch (error) {
        console.error('Error placing order:', error);
    }
}

// Fetch and display order history
async function fetchOrderHistory() {
    try {
        const orderHistory = await apiRequest('/order', 'GET');
        const orderList = document.getElementById('order-list');
        orderList.innerHTML = '';

        // Check if orderHistory.data exists and is an array
        if (orderHistory && Array.isArray(orderHistory.data) && orderHistory.data.length > 0) {
            orderHistory.data.forEach(order => {
                const li = document.createElement('li');
                li.textContent = `Order ID: ${order.order_id},Customer Name: ${order.customer_name}, Customer ID: ${order.customer_id}, Item ID: ${order.item_id}, Quantity: ${order.quantity}, Date: ${order.order_date}`;
                orderList.appendChild(li);
            });
            console.log(orderHistory);
        } else {
            orderList.innerHTML = '<li>No orders found.</li>'; // Inform user if no orders exist
        }
    } catch (error) {
        console.error('Error fetching order history:', error);
    }
}

// Event listener for the form
document.getElementById('place-order-form').addEventListener('submit', async (event) => {
    event.preventDefault();
    const customerId = parseInt(event.target.customerId.value);
    const itemId = parseInt(event.target.itemId.value);
    const quantity = parseInt(event.target.quantity.value);
    const orderDate = event.target.orderDate.value;

    await placeOrder(customerId, itemId, quantity, orderDate);
});

// Load order history when the page loads
document.addEventListener('DOMContentLoaded', async () => {
    await fetchOrderHistory();
});
