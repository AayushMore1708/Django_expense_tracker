function addAmount(amount) {
    fetch('/expenses/add_amount/' + amount + '/')
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error(error));
}

function subtractAmount(amount) {
    fetch('/expenses/subtract_amount/' + amount + '/')
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error(error));
}

function animateTotalAmount() {
    fetch('/expenses/animate_total_amount/')
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error(error));
}

function renderCalendar(year) {
    fetch('/expenses/render_calendar/' + year + '/')
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error(error));
}