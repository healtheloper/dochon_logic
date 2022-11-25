const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const input = [];

const solution = (input) => {
  let answer = 0;
  const [mn, ...arrays] = input;
  const [m, n] = mn.split(' ').map((v) => +v);
  const array = arrays.map((v) => v.split(' ').map((v) => +v));

  const first = [];
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (array[i][j] === 1) first.push([i, j]);
    }
  }

  const bfs = () => {
    const q = [first];
    let count = 0;
    const dx = [1, -1, 0, 0];
    const dy = [0, 0, 1, -1];

    while (q.length) {
      const tomatos = q.shift();
      const newTomatos = [];
      for (const [t1, t2] of tomatos) {
        for (let i = 0; i < 4; i++) {
          const x = t1 + dx[i];
          const y = t2 + dy[i];
          if (x >= 0 && x < n && y >= 0 && y < m && array[x][y] === 0) {
            array[x][y] = 1;
            newTomatos.push([x, y]);
          }
        }
      }
      if (newTomatos.length) {
        q.push(newTomatos);
        count += 1;
      }
    }

    return count;
  };
  const count = bfs();

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (array[i][j] === 0) return -1;
    }
  }

  return count;
};

rl.on('line', (answer) => {
  input.push(answer.trim());
}).on('close', () => {
  console.log(solution(input));
});
