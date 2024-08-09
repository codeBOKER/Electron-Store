document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.cart-card-item input[type="number"]').forEach(input => {
        input.addEventListener('change', function() {
            const itemId = this.closest('.cart-card-item').getAttribute('data-item-id');
            const quantity = this.value;

            fetch(`/update-cart/${itemId}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({ quantity: quantity })
            })
            .then(response => response.json())
            .then(data => {
                // Handle the response data
                console.log(data);
            });
        });
    });

    document.querySelectorAll('.remove-button').forEach(button => {
        button.addEventListener('click', function() {
            const itemId = this.getAttribute('data-item-id');

            fetch(`/remove-from-cart/${itemId}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({})
            })
            .then(response => response.json())
            .then(data => {
                // Handle the response data
                console.log(data);
                document.querySelector(`.cart-card-item[data-item-id="${itemId}"]`).remove();
            });
        });
    });

    document.getElementById('whatsapp-button').addEventListener('click', function() {
        let cartDetails = 'Your Cart:\n\n';
        document.querySelectorAll('.cart-card-item').forEach(item => {
            const itemName = item.querySelector('.cart-card-name').textContent;
            const itemQuantity = item.querySelector('input[type="number"]').value;
            cartDetails += `${itemName} - Quantity: ${itemQuantity}\n`;
        });

        const whatsappUrl = `https://wa.me/00967770026665/?text=${encodeURIComponent(cartDetails)}`;
        window.open(whatsappUrl, '_blank');
    });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}