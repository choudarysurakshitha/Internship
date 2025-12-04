const BASE_URL = "http://127.0.0.1:3000";

// SECTION SWITCH
function showSection(id) {
    document.querySelectorAll(".section").forEach(sec => sec.classList.remove("active"));
    document.getElementById(id).classList.add("active");
    document.querySelectorAll(".sidebar ul li").forEach(li => li.classList.remove("active"));
    event.target.classList.add("active");
}

// LOAD LOST ITEMS
async function loadLost() {
    const res = await fetch(`${BASE_URL}/lost`);
    const items = await res.json();
    const lostList = document.getElementById("lost-list");
    lostList.innerHTML = "";
    items.forEach(item => {
        const div = document.createElement("div");
        div.className = "item-card";
        div.innerHTML = `
            <h3>${item.item_name}</h3>
            <p>${item.description || ""}</p>
            <p><b>Location:</b> ${item.location_lost}</p>
            <button onclick="deleteLost(${item.id})">Delete</button>
            <button onclick="editLost(${item.id})">Edit</button>
        `;
        lostList.appendChild(div);
    });
    displayLatestLost(items);
}

// ADD LOST ITEM
async function addLost() {
    const item_name = document.getElementById("lost-name").value;
    const location_lost = document.getElementById("lost-location").value;
    const description = document.getElementById("lost-description").value;

    await fetch(`${BASE_URL}/lost`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ item_name, location_lost, description })
    });

    document.getElementById("lost-name").value = "";
    document.getElementById("lost-location").value = "";
    document.getElementById("lost-description").value = "";
    loadLost();
}

// DELETE & EDIT LOST
async function deleteLost(id) {
    await fetch(`${BASE_URL}/lost/${id}`, { method: "DELETE" });
    loadLost();
}

async function editLost(id) {
    const item = await (await fetch(`${BASE_URL}/lost/${id}`)).json();
    document.getElementById("lost-name").value = item.item_name;
    document.getElementById("lost-location").value = item.location_lost;
    document.getElementById("lost-description").value = item.description;

    const btn = document.querySelector("#lost-section .form-card button");
    btn.textContent = "Save Changes";
    btn.onclick = async () => {
        await fetch(`${BASE_URL}/lost/${id}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                item_name: document.getElementById("lost-name").value,
                location_lost: document.getElementById("lost-location").value,
                description: document.getElementById("lost-description").value
            })
        });
        btn.textContent = "Add Lost Item";
        btn.onclick = addLost;
        document.getElementById("lost-name").value = "";
        document.getElementById("lost-location").value = "";
        document.getElementById("lost-description").value = "";
        loadLost();
    };
}

// LOAD FOUND ITEMS
async function loadFound() {
    const res = await fetch(`${BASE_URL}/found`);
    const items = await res.json();
    const foundList = document.getElementById("found-list");
    foundList.innerHTML = "";
    items.forEach(item => {
        const div = document.createElement("div");
        div.className = "item-card";
        div.innerHTML = `
            <h3>${item.item_name}</h3>
            <p>${item.description || ""}</p>
            <p><b>Found At:</b> ${item.location_found}</p>
            <p><b>Email:</b> ${item.email || "Not provided"}</p>
            <button onclick="deleteFound(${item.id})">Delete</button>
            <button onclick="editFound(${item.id})">Edit</button>
        `;
        foundList.appendChild(div);
    });
    displayLatestFound(items);
}

// ADD FOUND ITEM
async function addFound() {
    const item_name = document.getElementById("found-name").value;
    const location_found = document.getElementById("found-location").value;
    const description = document.getElementById("found-description").value;
    const email = document.getElementById("found-email").value;

    await fetch(`${BASE_URL}/found`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ item_name, location_found, description, email })
    });

    document.getElementById("found-name").value = "";
    document.getElementById("found-location").value = "";
    document.getElementById("found-description").value = "";
    document.getElementById("found-email").value = "";
    loadFound();
}

// DELETE & EDIT FOUND
async function deleteFound(id) {
    await fetch(`${BASE_URL}/found/${id}`, { method: "DELETE" });
    loadFound();
}

async function editFound(id) {
    const item = await (await fetch(`${BASE_URL}/found/${id}`)).json();
    document.getElementById("found-name").value = item.item_name;
    document.getElementById("found-location").value = item.location_found;
    document.getElementById("found-description").value = item.description;
    document.getElementById("found-email").value = item.email;

    const btn = document.querySelector("#found-section .form-card button");
    btn.textContent = "Save Changes";
    btn.onclick = async () => {
        await fetch(`${BASE_URL}/found/${id}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                item_name: document.getElementById("found-name").value,
                location_found: document.getElementById("found-location").value,
                description: document.getElementById("found-description").value,
                email: document.getElementById("found-email").value
            })
        });
        btn.textContent = "Add Found Item";
        btn.onclick = addFound;
        document.getElementById("found-name").value = "";
        document.getElementById("found-location").value = "";
        document.getElementById("found-description").value = "";
        document.getElementById("found-email").value = "";
        loadFound();
    };
}

// DISPLAY LATEST ITEMS
function displayLatestLost(items) {
    const latestLost = document.getElementById("latest-lost");
    latestLost.innerHTML = "";
    items.slice(-3).forEach(item => {
        const div = document.createElement("div");
        div.className = "item-card";
        div.innerHTML = `<h4>${item.item_name}</h4><p>${item.description || ""}</p>`;
        latestLost.appendChild(div);
    });
}

function displayLatestFound(items) {
    const latestFound = document.getElementById("latest-found");
    latestFound.innerHTML = "";
    items.slice(-3).forEach(item => {
        const div = document.createElement("div");
        div.className = "item-card";
        div.innerHTML = `<h4>${item.item_name}</h4><p>${item.description || ""}</p>`;
        latestFound.appendChild(div);
    });
}

// INITIAL LOAD
window.onload = () => {
    loadLost();
    loadFound();
};








