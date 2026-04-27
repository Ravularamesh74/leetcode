var hasValidPath = function(grid) {
  const m = grid.length;
  const n = grid[0].length;

  const dirs = {
    1: [[0, -1], [0, 1]],
    2: [[-1, 0], [1, 0]],
    3: [[0, -1], [1, 0]],
    4: [[0, 1], [1, 0]],
    5: [[0, -1], [-1, 0]],
    6: [[0, 1], [-1, 0]]
  };

  const visited = Array.from({ length: m }, () => Array(n).fill(false));
  const queue = [[0, 0]];
  visited[0][0] = true;

  while (queue.length) {
    const [r, c] = queue.shift();

    if (r === m - 1 && c === n - 1) return true;

    for (const [dr, dc] of dirs[grid[r][c]]) {
      const nr = r + dr;
      const nc = c + dc;

      if (nr < 0 || nc < 0 || nr >= m || nc >= n || visited[nr][nc]) continue;

      const back = [-dr, -dc];

      if (dirs[grid[nr][nc]].some(([rdr, rdc]) => rdr === back[0] && rdc === back[1])) {
        visited[nr][nc] = true;
        queue.push([nr, nc]);
      }
    }
  }

  return false;
};