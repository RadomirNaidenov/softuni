function calc() {
    const num1InputEl = document.getElementById('num1');
    const num2InputEl = document.getElementById('num2');
    const resutInputEl = document.getElementById('sum');

    const num1 = Number(num1InputEl.value);
    const num2 = Number(num2InputEl.value);

    resutInputEl.value = num1 + num2
}