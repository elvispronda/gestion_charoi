document.getElementById("login-form").addEventListener("submit", async (e) => {
    e.preventDefault();

    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value.trim();
    const messageEl = document.getElementById("message");
    messageEl.classList.add("hidden");

    try {
        const response = await fetch("http://localhost:8000/login", {
            method: "POST",
            headers: { "Content-Type": "application/x-www-form-urlencoded" },
            body: new URLSearchParams({ username, password })  // Send data as URL-encoded
        });

        if (!response.ok) {
            const error = await response.json();
            console.log("Error Details (Parsed):", JSON.stringify(error, null, 2));
            messageEl.textContent = error.detail || "Login failed.";
            messageEl.classList.remove("hidden");
            return;
        }

        const data = await response.json();
        console.log("Login Successful, Response Data:", JSON.stringify(data, null, 2));

        localStorage.setItem("access_token", data.access_token);
        localStorage.setItem("token_type", data.token_type);

        messageEl.classList.add("text-green-600");
        messageEl.textContent = "Login successful!";
        messageEl.classList.remove("hidden");

        setTimeout(() => {
            window.location.href = "/dashboard";
        }, 1000);

    } catch (err) {
        console.error("Login Error (Catch Block):", JSON.stringify(err, null, 2));
        messageEl.textContent = "Server error. Please try again.";
        messageEl.classList.remove("hidden");
    }
});




