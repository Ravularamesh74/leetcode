/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {

    let length = 0;
    let i = s.length - 1;

    // Skip trailing spaces
    while (i >= 0 && s[i] === ' ') {
        i--;
    }

    // Count last word length
    while (i >= 0 && s[i] !== ' ') {
        length++;
        i--;
    }

    return length;
};