((function () {

    "use strict"

    const $pathname = location.pathname;
    const $menuItems = document.querySelectorAll("#kt_app_sidebar_menu_wrapper .menu-link");

    $menuItems.forEach(($menuItem) => {
        const pathname = $pathname;
        console.log(pathname);

        if (pathname === $menuItem.getAttribute("data-web-link")) {
            $menuItem.classList.add("menu-active");
        }
    })
})())