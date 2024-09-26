/* static/scripts.js */

// Display success or error messages after form submission
document.addEventListener('DOMContentLoaded', function() {
    const messages = document.querySelectorAll('.message');
    messages.forEach(message => {
        setTimeout(() => {
            message.style.display = 'none';
        }, 3000); // Hide messages after 3 seconds
    });
});
