/**
 * @param {number} n
 * @return {string}
 */
var countAndSay = function(n) {
    let result = "1";

    for (let i = 2; i <= n; i++) {
        let temp = "";
        let count = 1;

        for (let j = 0; j < result.length; j++) {

            // Count same consecutive digits
            while (
                j < result.length - 1 &&
                result[j] === result[j + 1]
            ) {
                count++;
                j++;
            }

            // Append count + digit
            temp += count + result[j];

            // Reset count
            count = 1;
        }

        result = temp;
    }

    return result;
};