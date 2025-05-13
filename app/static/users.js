async function fetchUsers() {
    try {
        const response = await fetch('http://localhost:8000/users');
        if (!response.ok) throw new Error('Failed to fetch users');
        
        const users = await response.json();
        const tableBody = document.getElementById('userTable');

        users.forEach(user => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${user.id}</td>
                <td>${user.username}</td>
                <td>${user.email}</td>
            `;
            tableBody.appendChild(row);
        });
    } catch (error) {
        console.error(error);
    }
}

window.onload = fetchUsers;

