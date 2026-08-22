/**
 * @param {number} n
 * @return {boolean}
 */
var checkDivisibility = function(n) {
    let digitSum = 0;
    let digitProduct = 1;
    let temp = n;

    while (temp > 0) {
        const digit = temp % 10;
        digitSum += digit;
        digitProduct *= digit;
        temp = Math.floor(temp / 10);
    }

    const total = digitSum + digitProduct;
    return n % total === 0;
};