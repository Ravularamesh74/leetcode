var sortVowels = function(s) {
    const vowelsSet = new Set(['a','e','i','o','u']);
    const arr = s.split("");

    let vowels = [];
    let freq = {};
    let firstIndex = {};

    // Step 1: collect vowels + freq + first occurrence
    for (let i = 0; i < arr.length; i++) {
        let ch = arr[i];
        if (vowelsSet.has(ch)) {
            vowels.push(ch);
            freq[ch] = (freq[ch] || 0) + 1;

            if (!(ch in firstIndex)) {
                firstIndex[ch] = i;
            }
        }
    }

    // Step 2: sort vowels
    vowels.sort((a, b) => {
        if (freq[b] !== freq[a]) {
            return freq[b] - freq[a]; // higher freq first
        }
        return firstIndex[a] - firstIndex[b]; // earlier first
    });

    // Step 3: put back vowels
    let idx = 0;
    for (let i = 0; i < arr.length; i++) {
        if (vowelsSet.has(arr[i])) {
            arr[i] = vowels[idx++];
        }
    }

    return arr.join("");
};