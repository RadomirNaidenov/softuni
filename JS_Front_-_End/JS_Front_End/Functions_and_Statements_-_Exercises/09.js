function makeLoadingBar(num) {
    let percentCount = num / 10;
    let dotCount = (100 - num) / 10;
    
    if (num !== 100) {
        console.log(`${num}% [${'%'.repeat(percentCount)}${'.'.repeat(dotCount)}]`);
        console.log(`Still loading...`);
    } else {
        console.log(`${num}% Complete!`);
        console.log(`[${'%'.repeat(percentCount)}]`);
    }
}
