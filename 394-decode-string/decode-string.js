/**
 * @param {string} s
 * @return {string}
 */
var decodeString = function(s) {
    let countStack = [];
    let stringStack = [];
    let currentString = '';
    let currentNum = 0;

    for (let char of s) {
        if (!isNaN(char)) {
            // Build multi-digit numbers (e.g., '10', '100')
            currentNum = currentNum * 10 + Number(char);
        } else if (char === '[') {
            // Push current state to stacks and reset
            countStack.push(currentNum);
            stringStack.push(currentString);
            currentNum = 0;
            currentString = '';
        } else if (char === ']') {
            // Pop multiplier and previous context string
            let repeatCount = countStack.pop();
            let prevString = stringStack.pop();
            currentString = prevString + currentString.repeat(repeatCount);
        } else {
            // Append standard characters
            currentString += char;
        }
    }

    return currentString;
};