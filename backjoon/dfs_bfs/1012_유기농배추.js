const input = require('fs')
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split('\n');

const solution = (input) => {
  const [T, ...rest] = input;
  const cases = [];
  for (let i = 0; i < +T; i++) {
    const [M, N, K] = rest[0].split(' ').map((v) => +v);
    const testCase = rest.splice(0, K + 1);
    cases.push(testCase);
  }

  return cases
    .map((testCase) => {
      const [count, ...rest] = testCase;
      const [M, N] = count.split(' ').map((v) => +v);
      const row = new Array(M).fill(0);
      const m = new Array(N).fill(0).map(() => [...row]);
      const visited = new Array(N).fill(0).map(() => [...row]);
      let 벌레 = 0;

      const dfs = (rowIdx, colIdx) => {
        const dx = [1, -1, 0, 0];
        const dy = [0, 0, 1, -1];
        for (let i = 0; i < 4; i++) {
          const x = rowIdx + dx[i];
          const y = colIdx + dy[i];
          const isXRange = x >= 0 && x < N;
          const isYRange = y >= 0 && y < M;
          if (isXRange && isYRange && m[x][y] === 1 && visited[x][y] === 0) {
            visited[x][y] = 1;
            dfs(x, y);
          }
        }
      };
      rest.forEach((position) => {
        const [x, y] = position.split(' ').map((v) => +v);
        m[y][x] = 1;
      });

      m.forEach((row, rowIdx) => {
        row.forEach((col, colIdx) => {
          const 땅 = m[rowIdx][colIdx];
          if (땅 === 1 && visited[rowIdx][colIdx] === 0) {
            dfs(rowIdx, colIdx);
            벌레 += 1;
          }
        });
      });

      return 벌레;
    })
    .join('\n');
};

console.log(solution(input));
