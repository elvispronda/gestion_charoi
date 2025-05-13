document.getElementById("login-form").addEventListener("submit", async (e) => {
    e.preventDefault();

    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value.trim();
    const messageEl = document.getElementById("message");
    messageEl.classList.add("hidden");

    try {
        const response = await fetch("http://localhost:8000/login", {
            method: "POST",
            headers: { 
                "Content-Type": "application/x-www-form-urlencoded",
                "Accept": "application/json"  // Ensure JSON response
            },
            body: new URLSearchParams({ username, password })
        });

        if (!response.ok) {
            const error = await response.json();
            console.log("Error Details (Parsed):", JSON.stringify(error));  // Properly log the error object

            // Handle error and display the message
            if (error.detail) {
                messageEl.textContent = `Error: ${error.detail}`;
            } else {
                messageEl.textContent = `Unexpected error occurred during login.`;
            }
            messageEl.classList.remove("hidden");
            return;
        }

        const data = await response.json();
        console.log("Login Successful, Response Data:", JSON.stringify(data));  // Properly log the success response

        // Save the token to local storage
        localStorage.setItem("access_token", data.access_token);
        localStorage.setItem("token_type", data.token_type);

        messageEl.classList.add("text-green-600");
        messageEl.textContent = "Login successful!";
        messageEl.classList.remove("hidden");

        // Redirect to the dashboard after a short delay
        setTimeout(() => {
            window.location.href = "/dashboard";
        }, 1000);

    } catch (err) {
        console.error("Login Error (Catch Block):", err);  // Catch any unexpected errors
        messageEl.textContent = "Server error. Please try again.";
        messageEl.classList.remove("hidden");
    }
});


