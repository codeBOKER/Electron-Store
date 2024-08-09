document.addEventListener('DOMContentLoaded', function() {
    const csrfToken = document.getElementById('csrf-token').value;
  
    fetch('/get-cart-item-count/')
    .then(response => response.json())
    .then(data => {
        document.getElementById('cart-item-count').textContent = data.cartItemCount;
        document.getElementById('cart-item-count-cart').textContent = data.cartItemCount;
    })
    .catch(error => {
        console.error('Error fetching cart item count:', error);
    });
  
document.querySelectorAll('.add-to-cart-button').forEach(button => {
    button.addEventListener('click', function() {
        const itemId = this.closest('.add-to-cart-form').getAttribute('data-item-id');
        const item = this.closest('.add-to-cart-form').getAttribute('data-item');
        fetch(`/add-to-cart/${item}/${itemId}/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken,
                'Content-Type': 'application/json'
            }
        })
        .then(response => {
            if (response.ok) {
                fetch('/get-cart-item-count/')
                .then(response => response.json())
                .then(data => {
                    document.getElementById('cart-item-count').textContent = data.cartItemCount;
                })
                .catch(error => {
                    console.error('Error fetching cart item count:', error);
                });
            } else {
                alert('Failed to add item to cart');
            }
        })
          .catch(error => {
              console.error('Error:', error);
          });
      });
  });
});

