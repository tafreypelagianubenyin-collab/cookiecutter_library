document.addEventListener("DOMContentLoaded", () => {
    const menuButton = document.getElementById("mobile-menu-button");
    const mobileMenu = document.getElementById("mobile-menu");

    if (menuButton && mobileMenu) {
        menuButton.addEventListener("click", () => {
            mobileMenu.classList.toggle("hidden");

            const isOpen = !mobileMenu.classList.contains("hidden");
            menuButton.setAttribute("aria-expanded", isOpen);
        });
    }
});
