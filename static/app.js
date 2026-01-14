const tabs = document.querySelectorAll(".tab");

function setActiveTab() {
    const path = window.location.pathname;

    tabs.forEach((tab) => {
        const link = tab.querySelector("a");
        const href = link ? link.getAttribute("href") : null;

        // Remove active class from all tabs initially
        tab.classList.remove("active");

        // Add active class if the path matches the href
        // We use exact match or check if it's the home page
        if (href && (href === path || (href !== '/' && path.startsWith(href)))) {
            tab.classList.add("active");
        }
    });
}

// Set active tab on page load
document.addEventListener("DOMContentLoaded", setActiveTab);

// Handle clicks for visual feedback (especially for '#' links)
tabs.forEach((tab) => {
    tab.addEventListener("click", () => {
        tabs.forEach(t => t.classList.remove("active"));
        tab.classList.add("active");
    });
});