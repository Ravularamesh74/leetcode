function findLadders(beginWord: string, endWord: string, wordList: string[]): string[][] {
    const wordSet = new Set<string>(wordList);
    if (!wordSet.has(endWord)) return [];

    // Map each word to its parents in the shortest path DAG
    const parentMap = new Map<string, string[]>();
    // Tracks distance from beginWord to each visited word
    const distance = new Map<string, number>();
    
    // BFS initialization
    const queue: string[] = [beginWord];
    distance.set(beginWord, 0);
    let found = false;

    while (queue.length > 0) {
        const currentLevelSize = queue.length;

        for (let i = 0; i < currentLevelSize; i++) {
            const word = queue.shift()!;
            const currentDist = distance.get(word)!;

            if (word === endWord) {
                found = true;
            }

            // Generate all possible valid one-letter transformations
            for (let j = 0; j < word.length; j++) {
                for (let c = 97; c <= 122; c++) {
                    const char = String.fromCharCode(c);
                    if (char === word[j]) continue;

                    const nextWord = word.slice(0, j) + char + word.slice(j + 1);

                    if (wordSet.has(nextWord)) {
                        // First time seeing this word
                        if (!distance.has(nextWord)) {
                            distance.set(nextWord, currentDist + 1);
                            parentMap.set(nextWord, [word]);
                            queue.push(nextWord);
                        } 
                        // Found another shortest path to an existing word at the current layer
                        else if (distance.get(nextWord)! === currentDist + 1) {
                            parentMap.get(nextWord)!.push(word);
                        }
                    }
                }
            }
        }

        if (found) break; // Reached endWord level; stop further BFS expansion
    }

    if (!found) return [];

    // DFS to reconstruct all paths from endWord back to beginWord
    const results: string[][] = [];

    function backtrack(currWord: string, path: string[]): void {
        if (currWord === beginWord) {
            results.push([beginWord, ...path]);
            return;
        }

        const parents = parentMap.get(currWord) || [];
        for (const parent of parents) {
            backtrack(parent, [currWord, ...path]);
        }
    }

    backtrack(endWord, []);
    return results;
}