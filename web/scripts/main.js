// Handle login
async function login() {
    const username = document.getElementById('username').value
    const password = document.getElementById('password').value

    const success = await eel.login(username, password)()
    if (success) {
        document.getElementById('login-screen').classList.add('hidden')
        document.getElementById('main-screen').classList.remove('hidden')
    } else {
        alert('Invalid credentials')
    }
}

// Handle drone connections
async function connectDrone(drone) {
    const success = await eel.connect_drone(drone)()
    if (success) {
        updateDroneStatus(drone, 'connected')
    }
}

// Show different sections
function showSection(section) {
    // Hide all sections
    document.querySelectorAll('.section').forEach(el => el.classList.add('hidden'))
    // Show selected section
    document.getElementById(`${section}-section`).classList.remove('hidden')
}

// Add these functions
function updateDroneStatus(drone, status) {
    const btn = document.querySelector(`[onclick="connectDrone('${drone}')"]`);
    if (status === 'connected') {
        btn.textContent = 'Disconnect';
        btn.classList.add('connected');
        updateDroneCount(1);
    } else {
        btn.textContent = 'Connect';
        btn.classList.remove('connected');
        updateDroneCount(-1);
    }
}

function updateDroneCount(change) {
    const countElement = document.querySelector('.drone-count');
    const currentCount = parseInt(countElement.textContent.split(':')[1].trim().split('/')[0]);
    countElement.textContent = `Drone(s) Connected: ${currentCount + change}/6`;
}

// Add more drone-specific functions as needed