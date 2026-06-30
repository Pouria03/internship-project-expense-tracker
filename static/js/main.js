document.addEventListener('DOMContentLoaded', function () {

    'use strict';

    // ============================================================
    // 1. Scroll-triggered Fade-in Animations
    // ============================================================
    (function initScrollAnimations() {
        var els = document.querySelectorAll('.fade-in, .fade-in-left, .fade-in-right, .fade-in-scale');
        if (!els.length) return;

        var observer = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (!entry.isIntersecting) return;
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            });
        }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

        els.forEach(function (el) { observer.observe(el); });
    })();


    // ============================================================
    // 2. Navbar Glass Effect on Scroll
    // ============================================================
    (function initNavbarScroll() {
        var navbar = document.querySelector('.navbar-glass');
        if (!navbar) return;

        window.addEventListener('scroll', function () {
            var dense = window.scrollY > 50;
            navbar.style.background = dense ? 'rgba(15, 12, 41, 0.85)' : 'rgba(15, 12, 41, 0.6)';
            navbar.style.backdropFilter = dense ? 'blur(24px)' : 'blur(20px)';
        });
    })();


    // ============================================================
    // 3. Animated Stat Counters
    // ============================================================
    (function initStatCounters() {
        var statValues = document.querySelectorAll('.stat-value');
        if (!statValues.length) return;

        var observer = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (!entry.isIntersecting) return;
                var el = entry.target;
                var raw = el.textContent.trim();
                var num = parseInt(raw.replace(/[^0-9]/g, ''));
                if (isNaN(num)) return;

                var suffix = raw.replace(/[0-9,]/g, '').trim();
                var step = num / 30;
                var cur = 0;
                var timer = setInterval(function () {
                    cur += step;
                    if (cur >= num) {
                        clearInterval(timer);
                        el.textContent = num.toLocaleString() + ' ' + suffix;
                    } else {
                        el.textContent = Math.round(cur).toLocaleString() + ' ' + suffix;
                    }
                }, 33);
                observer.unobserve(el);
            });
        }, { threshold: 0.3 });

        statValues.forEach(function (el) { observer.observe(el); });
    })();


    // ============================================================
    // 4. Table Row Staggered Entrance
    // ============================================================
    (function initTableRows() {
        var tables = document.querySelectorAll('.glass-table');
        if (!tables.length) return;

        tables.forEach(function (table) {
            var rows = table.querySelectorAll('tbody tr');
            rows.forEach(function (row, i) {
                row.style.opacity = '0';
                row.style.transform = 'translateY(10px)';
                row.style.transition = 'opacity 0.4s ease, transform 0.4s ease, background 0.3s ease';
                row.style.transitionDelay = (i * 0.05) + 's';
            });

            var observer = new IntersectionObserver(function (entries) {
                entries.forEach(function (entry) {
                    if (!entry.isIntersecting) return;
                    var rowList = entry.target.querySelectorAll('tbody tr');
                    rowList.forEach(function (row) {
                        row.style.opacity = '1';
                        row.style.transform = 'translateY(0)';
                    });
                    observer.unobserve(entry.target);
                });
            }, { threshold: 0.1 });

            observer.observe(table);
        });
    })();


    // ============================================================
    // 5. Form Input Focus Effect
    // ============================================================
    (function initInputEffects() {
        var inputs = document.querySelectorAll('.glass-input');
        inputs.forEach(function (input) {
            input.addEventListener('focus', function () {
                var wrapper = input.closest('.mb-3') || input.parentElement;
                if (wrapper) {
                    wrapper.style.transform = 'translateX(4px)';
                    wrapper.style.transition = 'transform 0.2s ease';
                }
            });
            input.addEventListener('blur', function () {
                var wrapper = input.closest('.mb-3') || input.parentElement;
                if (wrapper) wrapper.style.transform = 'translateX(0)';
            });
        });
    })();


    // ============================================================
    // 6. Alert Smooth Dismiss
    // ============================================================
    (function initAlertDismiss() {
        var alerts = document.querySelectorAll('.glass-alert');
        alerts.forEach(function (alert) {
            var btn = alert.querySelector('.btn-close');
            if (!btn) return;
            btn.addEventListener('click', function (e) {
                e.preventDefault();
                alert.style.transition = 'opacity 0.3s ease, transform 0.3s ease';
                alert.style.opacity = '0';
                alert.style.transform = 'translateY(-10px)';
                setTimeout(function () { alert.style.display = 'none'; }, 300);
            });
        });
    })();


    // ============================================================
    // 7. Jalali Date Picker (majidh1/JalaliDatePicker)
    // ============================================================
    if (typeof jalaliDatepicker !== 'undefined') {
        jalaliDatepicker.startWatch();
    }

});
