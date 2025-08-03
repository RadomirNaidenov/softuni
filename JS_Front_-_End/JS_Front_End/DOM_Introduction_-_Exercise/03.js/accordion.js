function toggle() {
    const btnClassEl = document.getElementsByClassName('button')[0];
    const textPrEl = document.getElementById('extra')

    if (btnClassEl.textContent === 'More') {
        textPrEl.style.display = 'block'
        btnClassEl.textContent = 'Less'
    } else if (btnClassEl.textContent === 'Less') {
        textPrEl.style.display = 'none'
        btnClassEl.textContent = 'More'
    }

}