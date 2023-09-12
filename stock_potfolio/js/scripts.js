// portfolio/static/portfolio/js/scripts.js
document.addEventListener('DOMContentLoaded', function () {
    const listItems = document.querySelectorAll('.stock-list li, .status-list li, .news-list li, .holding-list li');
    listItems.forEach(item => {
        item.addEventListener('click', () => {
            item.style.backgroundColor = '#007bff'; // Change background color on click
            item.style.color = 'white'; // Change text color on click
        });
    });
});
