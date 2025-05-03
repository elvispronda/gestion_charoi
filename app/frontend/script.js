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
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ username, password })
      });
  
      if (!response.ok) {
        const errorData = await response.json();
        messageEl.textContent = errorData.detail || "Login failed.";
        messageEl.classList.remove("hidden");
        return;
      }
  
      const data = await response.json();
      console.log("Login success:", data);
  
      // ✅ Save token if returned
      if (data.access_token) {
        localStorage.setItem("token", data.access_token);
        // Redirect if needed
        window.location.href = "/dashboard.html";
      }
    } catch (err) {
      console.error("Login error:", err);
      messageEl.textContent = "Server error. Please try again.";
      messageEl.classList.remove("hidden");
    }
  });