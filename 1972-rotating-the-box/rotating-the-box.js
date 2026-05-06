/**
 * @param {character[][]} boxGrid
 * @return {character[][]}
 */
var rotateTheBox = function(boxGrid) {
    let m = boxGrid.length;
    let n = boxGrid[0].length;

    // Step 1: Make stones fall to the right
    for (let i = 0; i < m; i++) {
        let empty = n - 1;

        for (let j = n - 1; j >= 0; j--) {
            if (boxGrid[i][j] === '*') {
                empty = j - 1;
            } 
            else if (boxGrid[i][j] === '#') {
                // Move stone to the farthest empty spot
                [boxGrid[i][j], boxGrid[i][empty]] = [boxGrid[i][empty], boxGrid[i][j]];
                empty--;
            }
        }
    }

    // Step 2: Rotate 90 degrees clockwise
    let result = Array.from({ length: n }, () => Array(m).fill('.'));

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            result[j][m - 1 - i] = boxGrid[i][j];
        }
    }

    return result;
};