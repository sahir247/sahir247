// Handle form submission
document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    // Just for demo: check if username and password match
    if (username === "admin" && password === "password123") {
        alert("Login Successful!");
        // Redirect to a different page or dashboard
    } else {
        alert("Invalid credentials. Please try again.");
    }
});