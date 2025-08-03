function subtract() {
    const firstNameinputEl = document.getElementById('firstNumber');
    const secondNumberInputEl = document.getElementById('secondNumber');

    const resultspanEl = document.getElementById('result');

    let result = 0;

    result = Number(firstNameinputEl.value) - Number(secondNumberInputEl.value);

    resultspanEl.textContent = result
}