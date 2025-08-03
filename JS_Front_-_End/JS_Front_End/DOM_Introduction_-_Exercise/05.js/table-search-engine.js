function solve() {
    const rows = document.querySelectorAll('tbody tr');
    const searchValue = document.getElementById('searchField').value.toLowerCase();

    for (let row of rows) {
        row.classList.remove('select');

        if (row.textContent.toLowerCase().includes(searchValue)) {
            row.classList.add('select');
        }
    }
}