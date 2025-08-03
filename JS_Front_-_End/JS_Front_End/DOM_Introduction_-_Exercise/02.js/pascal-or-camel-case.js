function solve() {
    const textInputEl = document.getElementById('text');
    const convationinputEl = document.getElementById('naming-convention');
    const resultSpanEl = document.getElementById('result');

    const words = textInputEl.value.toLowerCase().split(' ');
    let result = '';

    if (convationinputEl.value === 'Camel Case') {
        result = words[0]
        for (let i = 1; i < words.length; i++) {
            result += words[i][0].toUpperCase() + words[i].slice(1);
        }
    } else if (convationinputEl.value === 'Pascal Case') {

        for (let word of words) {
            result += word[0].toUpperCase() + word.slice(1);
        }
    } else {
        result = 'Error!';
    }

    resultSpanEl.textContent = result;
}