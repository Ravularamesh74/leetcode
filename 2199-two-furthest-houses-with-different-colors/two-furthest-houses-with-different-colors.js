var maxDistance = function(colors) {
    let n = colors.length;
    let maxDist = 0;

    // Compare with first element
    for (let i = n - 1; i >= 0; i--) {
        if (colors[i] !== colors[0]) {
            maxDist = Math.max(maxDist, i);
            break;
        }
    }

    // Compare with last element
    for (let i = 0; i < n; i++) {
        if (colors[i] !== colors[n - 1]) {
            maxDist = Math.max(maxDist, n - 1 - i);
            break;
        }
    }

    return maxDist;
};