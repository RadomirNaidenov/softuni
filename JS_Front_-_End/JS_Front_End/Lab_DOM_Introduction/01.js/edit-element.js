function editElement(element, word, replaceWord) {
    let htmlContent = element.textContent;
    htmlContent = htmlContent.replaceAll(word, replaceWord);

    element.textContent = htmlContent
}