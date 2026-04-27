var letterCombinations = function(digits) {
  if (!digits.length) return [];

  const map = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
  };

  const res = [];

  function backtrack(index, path) {
    // base case
    if (index === digits.length) {
      res.push(path);
      return;
    }

    const letters = map[digits[index]];

    for (let ch of letters) {
      backtrack(index + 1, path + ch);
    }
  }

  backtrack(0, "");
  return res;
};