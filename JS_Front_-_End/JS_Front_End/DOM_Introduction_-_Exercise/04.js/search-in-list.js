function solve() {
    const townsliEls = document.querySelectorAll('#towns li');
    const searchInputEl = document.getElementById('searchText');
    const resultDivEl = document.getElementById('result');

    let counter = 0;

    for (let townliEl of townsliEls) {
        townliEl.style.textDecoration = 'none';
        townliEl.style.fontWeight = 'normal';
    }

    for (let townliEl of townsliEls) {
        if (townliEl.textContent.includes(searchInputEl.value)) {
            counter += 1;
            townliEl.style.textDecoration = 'underline'
            townliEl.style.fontWeight = 'bold'
        }
    }


    resultDivEl.textContent = `${counter} matches found`
}