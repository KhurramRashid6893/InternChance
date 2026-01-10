let currentData = {}; // Store data for AI improvement step

// Modal Logic
function openChat() {
    document.getElementById('chat-modal').style.display = 'block';
}
function closeChat() {
    document.getElementById('chat-modal').style.display = 'none';
}
// Close modal if clicking outside
window.onclick = function(event) {
    if (event.target == document.getElementById('chat-modal')) {
        closeChat();
    }
}

// Prediction Logic
document.getElementById('prediction-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    // 1. Gather Data
    currentData = {
        cgpa: document.getElementById('cgpa').value,
        dsa: document.getElementById('dsa').value,
        projects: document.getElementById('projects').value,
        hackathons: document.getElementById('hackathons').value,
        certs: document.getElementById('certs').value
    };

    // 2. Fetch Prediction
    const response = await fetch('/predict', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(currentData)
    });
    
    const data = await response.json();
    
    // 3. Update UI
    document.getElementById('initial-state').classList.add('hidden');
    document.getElementById('prediction-result').classList.remove('hidden');
    document.getElementById('score-val').innerText = data.probability + "%";
    
    // Hide previous analysis if any
    document.getElementById('ai-analysis-section').classList.add('hidden');
});

// Improvement Logic (The new User Request)
async function getImprovementPlan() {
    const aiSection = document.getElementById('ai-analysis-section');
    const contentDiv = document.getElementById('ai-content');
    
    aiSection.classList.remove('hidden');
    contentDiv.innerHTML = '<div style="text-align:center; padding:20px;"><i class="fa-solid fa-spinner fa-spin fa-2x"></i><p>Consulting AI Coach...</p></div>';

    // Scroll to section
    aiSection.scrollIntoView({behavior: "smooth"});

    const response = await fetch('/analyze', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(currentData)
    });
    
    const data = await response.json();
    // Injecting HTML directly as the backend formats it
    contentDiv.innerHTML = data.analysis;
}

// Chat Functionality
async function sendChat() {
    const input = document.getElementById('chat-msg');
    const window = document.getElementById('chat-window');
    const msg = input.value;
    if(!msg) return;

    // Add User Message
    const userDiv = document.createElement('div');
    userDiv.className = 'message user-msg';
    userDiv.innerText = msg;
    window.appendChild(userDiv);
    input.value = "";
    window.scrollTop = window.scrollHeight;

    // Fetch AI Response
    const res = await fetch('/chat', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({message: msg})
    });
    const data = await res.json();

    // Add Bot Message
    const botDiv = document.createElement('div');
    botDiv.className = 'message bot-msg';
    botDiv.innerText = data.response;
    window.appendChild(botDiv);
    window.scrollTop = window.scrollHeight;
}