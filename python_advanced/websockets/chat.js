const socket = new WebSocket(`ws://${window.location.host}/ws`);

const statusEl = document.getElementById("status");
const messagesEl = document.getElementById("messages");
const form = document.getElementById("chat-form");
const input = document.getElementById("message-input");

function addMessage(text, kind) {
    const el = document.createElement("div");
    el.className = `message ${kind}`;
    const time = new Date().toLocaleTimeString();
    el.textContent = `[${time}] ${text}`;
    messagesEl.appendChild(el);
    messagesEl.scrollTop = messagesEl.scrollHeight;
}

socket.onopen = () => {
    statusEl.textContent = "Connected";
    statusEl.className = "connected";
};

socket.onmessage = (event) => {
    addMessage(event.data, "received");
};

socket.onclose = () => {
    statusEl.textContent = "Disconnected";
    statusEl.className = "disconnected";
};

form.addEventListener("submit", (event) => {
    event.preventDefault();
    const text = input.value;
    if (!text) {
        return;
    }
    socket.send(text);
    addMessage(text, "sent");
    input.value = "";
});
