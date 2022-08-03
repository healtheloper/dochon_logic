const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = (input) => {
  const [N, K] = input.split(' ').map((v) => +v);

  const array = new Array(100_000 + 1).fill(1e9);

  const q = [N];
  array[N] = 1;
  const bfs = () => {
    while (q.length) {
      const front = q.shift();
      if (front === K) break;
      if (front - 1 >= 0) {
        if (array[front - 1] === 1e9) {
          array[front - 1] = array[front] + 1;
          q.push(front - 1);
        }
      }
      if (front + 1 <= 100_000) {
        if (array[front + 1] === 1e9) {
          array[front + 1] = array[front] + 1;
          q.push(front + 1);
        }
      }
      if (front * 2 <= 100_000) {
        if (array[front * 2] === 1e9) {
          array[front * 2] = array[front] + 1;
          q.push(front * 2);
        }
      }
    }
  };

  bfs();
  return array[K] - 1;
};

rl.on('line', (answer) => {
  console.log(solution(answer));
  rl.close();
});
