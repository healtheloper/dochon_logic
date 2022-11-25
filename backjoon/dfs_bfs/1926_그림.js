const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const input = [];

const solution = (input) => {
  let answer = 0;
  let paintCount = 0;
  const [nm, ...arrays] = input;
  const [n, m] = nm.split(' ').map((v) => +v);

  const array = arrays.map((v) => v.split(' ').map((v) => +v));
  const visited = new Array(n).fill(0).map((v) => new Array(m).fill(0));

  const bfs = (a, b) => {
    if (visited[a][b] || array[a][b] === 0) return 0;
    paintCount += 1;
    visited[a][b] = 1;
    let count = 1;
    const q = [[a, b]];
    const dx = [1, -1, 0, 0];
    const dy = [0, 0, 1, -1];
    while (q.length) {
      const [e1, e2] = q.shift();
      for (let i = 0; i < 4; i++) {
        const x = e1 + dx[i];
        const y = e2 + dy[i];
        if (
          x >= 0 &&
          x < n &&
          y >= 0 &&
          y < m &&
          array[x][y] === 1 &&
          visited[x][y] === 0
        ) {
          visited[x][y] = 1;
          q.push([x, y]);
          count += 1;
        }
      }
    }
    return count;
  };

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      answer = Math.max(answer, bfs(i, j));
    }
  }

  return [paintCount, answer].join('\n');
};

rl.on('line', (answer) => {
  input.push(answer.trim());
}).on('close', () => {
  console.log(solution(input));
});
