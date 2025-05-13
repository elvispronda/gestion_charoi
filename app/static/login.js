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
                "Content-Type": "application/json"  // Set the content type to JSON
            },
            body: JSON.stringify({
                email: username,  // Assuming email is used as the username
                password: password
            })
        });

        if (!response.ok) {
            const error = await response.json();
            // Log the error in JSON format to check the details
            console.log("Error Details (Parsed):", JSON.stringify(error, null, 2));  
            messageEl.textContent = error.detail || "Login failed.";  // Display error message
            messageEl.classList.remove("hidden");
            return;
        }

        const data = await response.json();
        // Log the response properly to check the response object
        console.log("Login Successful, Response Data:", JSON.stringify(data, null, 2));  
        
        // Save the token to local storage
        localStorage.setItem("access_token", data.access_token);
        localStorage.setItem("token_type", data.token_type);

        messageEl.classList.add("text-green-600");
        messageEl.textContent = "Login successful!";
        messageEl.classList.remove("hidden");

        // Redirect to the dashboard after a short delay
        setTimeout(() => {
            window.location.href = "/dashboard";  // Redirect to the dashboard page
        }, 1000);

    } catch (err) {
        // Log the error properly to inspect what went wrong in the catch block
        console.error("Login Error (Catch Block):", JSON.stringify(err, null, 2));  
        messageEl.textContent = "Server error. Please try again.";
        messageEl.classList.remove("hidden");
    }
});






