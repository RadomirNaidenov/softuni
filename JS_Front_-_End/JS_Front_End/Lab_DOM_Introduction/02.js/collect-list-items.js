function extractText() {
    const liEls = document.querySelectorAll('#items, li');
    const textareaEl = document.getElementById('result');

    for (const liEl of liEls) {
        const liText = liEl.textContent;
        textareaEl.textContent += liText + '\n';
    }
    
}