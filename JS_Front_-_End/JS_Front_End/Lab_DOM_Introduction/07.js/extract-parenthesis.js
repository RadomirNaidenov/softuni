function extract(targedElId) {
    const targetEl = document.getElementById(targedElId);
    const content = targetEl.textContent;
    
    const pattern = /\(.+?\)/g;
    const matches = content.match(pattern);

    const formatedMatches = matches.map(match => match.substring(1, match.length - 1))

    return formatedMatches.join('; ')
}