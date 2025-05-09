
  document.getElementById("login-form").addEventListener("submit", async (e) => {
    e.preventDefault();

    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value.trim();
    const messageEl = document.getElementById("message");
    messageEl.classList.add("hidden");

    try {
      const response = await fetch("http://127.0.0.1:8000/auth/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password })
      });

      if (!response.ok) {
        const error = await response.json();
        messageEl.textContent = error.detail || "Login failed.";
        messageEl.classList.remove("hidden");
        return;
      }

      const data = await response.json();
      localStorage.setItem("token", data.access_token); // Save token in localStorage
      messageEl.classList.add("text-green-600");
      messageEl.textContent = "Login successful!";
      messageEl.classList.remove("hidden");

      // Redirect to the dashboard after a short delay
      setTimeout(() => {
        window.location.href = "dashboard.html"; // Update the path as needed
      }, 1000);

    } catch (err) {
      messageEl.textContent = "Server error. Please try again.";
      messageEl.classList.remove("hidden");
    }
  });
