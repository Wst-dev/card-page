document.addEventListener('DOMContentLoaded', function () {
    const sections = document.querySelectorAll('.section');

    window.onscroll = function () {
        sections.forEach(section => {
            if (isInViewport(section)) {
                section.style.opacity = '1';
            } else {
                section.style.opacity = '0.5';
            }
        });
    };
});

function isInViewport(element) {
    const rect = element.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}