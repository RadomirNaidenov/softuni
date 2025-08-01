function sumTable() {
    const priceTdEls = Array.from(document.querySelectorAll('tbody tr td:nth-child(2)'));
    
    const sumTdEl = priceTdEls.pop();
    let sum = 0

    for (const priceTdEl of priceTdEls) {
        sum += Number(priceTdEl.textContent)
    }

    sumTdEl.textContent = sum

}