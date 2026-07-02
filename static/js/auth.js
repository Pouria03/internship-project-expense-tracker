document.addEventListener('DOMContentLoaded', function () {
    'use strict';

    document.querySelectorAll('.glass-card form input, .glass-card form select, .glass-card form textarea').forEach(function (el) {
        el.classList.add('glass-input');
        el.style.width = '100%';
    });
});
