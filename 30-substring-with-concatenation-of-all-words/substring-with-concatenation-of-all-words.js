
var findSubstring = function(s, words) {

    if (!s || !words.length) return [];

    const wordLen = words[0].length;
    const totalWords = words.length;
    const windowLen = wordLen * totalWords;

    const wordCount = new Map();

    for (let word of words) {
        wordCount.set(word, (wordCount.get(word) || 0) + 1);
    }

    const result = [];

    // Try every offset
    for (let i = 0; i < wordLen; i++) {

        let left = i;
        let right = i;

        let seen = new Map();
        let count = 0;

        while (right + wordLen <= s.length) {

            let word = s.substring(right, right + wordLen);
            right += wordLen;

            // valid word
            if (wordCount.has(word)) {

                seen.set(word, (seen.get(word) || 0) + 1);
                count++;

                // too many duplicates
                while (seen.get(word) > wordCount.get(word)) {

                    let leftWord = s.substring(left, left + wordLen);

                    seen.set(leftWord, seen.get(leftWord) - 1);

                    left += wordLen;
                    count--;
                }

                // found valid window
                if (count === totalWords) {

                    result.push(left);

                    let leftWord = s.substring(left, left + wordLen);

                    seen.set(leftWord, seen.get(leftWord) - 1);

                    left += wordLen;
                    count--;
                }

            } else {

                // reset window
                seen.clear();
                count = 0;
                left = right;
            }
        }
    }

    return result;
};