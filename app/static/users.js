async function fetchUsers() {
    try {
        const token = localStorage.getItem('access_token');
        const tokenType = localStorage.getItem('token_type');  // Usually 'bearer'
        
        if (!token || !tokenType) throw new Error('No access token found');

        const response = await fetch('http://localhost:8000/users', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `${tokenType} ${token}`  // Correctly formatted token header
            }
        });

        if (!response.ok) throw new Error(`Error: ${response.statusText}`);
        
        const users = await response.json();
        const tableBody = document.getElementById('userTable');

        // Clear previous table data
        tableBody.innerHTML = '';

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
        console.error('Error fetching users:', error.message);
        alert('Failed to fetch users. Please check the console for more details.');
    }
}

window.onload = fetchUsers;
