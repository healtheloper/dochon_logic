const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const input = [];

const solution = (input) => {
  const [nm, ...arrays] = input;
  const [n, m] = nm.split(' ').map((v) => +v);
  const array = arrays.map((v) => v.split('').map((v) => +v));

  const bfs = () => {
    const q = [[0, 0]];
    const dx = [1, -1, 0, 0];
    const dy = [0, 0, 1, -1];
    while (q.length) {
      const [e1, e2] = q.shift();
      for (let i = 0; i < 4; i++) {
        const x = e1 + dx[i];
        const y = e2 + dy[i];
        if (x >= 0 && x < n && y >= 0 && y < m && array[x][y] === 1) {
          array[x][y] = array[e1][e2] + 1;
          q.push([x, y]);
        }
      }
    }
  };
  bfs();
  return array[n - 1][m - 1];
};

rl.on('line', (answer) => {
  input.push(answer.trim());
}).on('close', () => {
  console.log(solution(input));
});
