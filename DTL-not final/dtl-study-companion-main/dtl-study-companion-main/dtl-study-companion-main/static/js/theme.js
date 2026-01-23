// Load theme on startup
window.onload = function () {

    let theme = localStorage.getItem("theme");

    if (!theme) {
        // Default = DARK
        theme = "dark";
        localStorage.setItem("theme", "dark");
    }

    if (theme === "dark") {
        document.body.classList.add("dark-theme");
    } else {
        document.body.classList.remove("dark-theme");
    }
};


// Toggle theme button
function toggleTheme() {

    if (document.body.classList.contains("dark-theme")) {

        document.body.classList.remove("dark-theme");
        localStorage.setItem("theme", "light");

    } else {

        document.body.classList.add("dark-theme");
        localStorage.setItem("theme", "dark");
    }
}
