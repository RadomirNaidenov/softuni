function colorize() {
    const trEls = document.querySelectorAll('tbody tr');
    
    trEls.forEach((trEl, idx) => {
        if (idx % 2 !== 0) {
            trEl.style.background = 'Teal'
        }
    })
    
}