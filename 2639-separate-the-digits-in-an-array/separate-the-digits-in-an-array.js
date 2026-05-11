/**
 * @param {number[]} nums
 * @return {number[]}
 */
var separateDigits = function(nums) {
    let result = [];

    for (let num of nums) {
        let digits = num.toString(); // convert to string
        
        for (let ch of digits) {
            result.push(Number(ch)); // convert back to number
        }
    }

    return result;
};