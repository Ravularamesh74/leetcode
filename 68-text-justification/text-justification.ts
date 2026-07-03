function fullJustify(words: string[], maxWidth: number): string[] {
    const result: string[] = [];
    let i = 0;

    while (i < words.length) {
        let lineLength = words[i].length;
        let j = i + 1;

        // Determine how many words can fit into the current line
        while (j < words.length && lineLength + 1 + words[j].length <= maxWidth) {
            lineLength += 1 + words[j].length;
            j++;
        }

        const currentLineWords = words.slice(i, j);
        const numWords = currentLineWords.length;
        const totalWordChars = currentLineWords.reduce((sum, word) => sum + word.length, 0);
        const totalSpaces = maxWidth - totalWordChars;

        let line = "";

        // Case 1: Last line or line contains only 1 word -> Left Justified
        if (j === words.length || numWords === 1) {
            line = currentLineWords.join(" ");
            const remainingSpaces = maxWidth - line.length;
            line += " ".repeat(remainingSpaces);
        } 
        // Case 2: Middle line with multiple words -> Fully Justified
        else {
            const numGaps = numWords - 1;
            const baseSpaces = Math.floor(totalSpaces / numGaps);
            const extraSpaces = totalSpaces % numGaps;

            for (let k = 0; k < numGaps; k++) {
                // Assign an extra space to leftmost slots if remainder exists
                const spacesToApply = baseSpaces + (k < extraSpaces ? 1 : 0);
                line += currentLineWords[k] + " ".repeat(spacesToApply);
            }
            // Append the last word of the line without trailing spaces
            line += currentLineWords[numWords - 1];
        }

        result.push(line);
        i = j; // Move onto the next set of words
    }

    return result;
}
