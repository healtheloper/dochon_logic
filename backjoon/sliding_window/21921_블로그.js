const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const input = [];

const solution = (input) => {
  const [nx, rest] = input;
  const [N, X] = nx.split(' ').map((v) => +v);
  const counts = rest.split(' ').map((v) => +v);
  let max = -1;
  let count = 0;
  let result = 0;

  for (let i = 0; i < N - X + 1; i++) {
    if (i == 0) {
      for (let j = 0; j < X; j++) {
        result += counts[i + j];
      }
    } else {
      result -= counts[i - 1];
      result += counts[i + X - 1];
    }
    if (max === result) {
      count += 1;
    } else if (max < result) {
      count = 1;
      max = result;
    }
  }

  return max === 0 ? 'SAD' : [max, count].join('\n');
};

rl.on('line', (answer) => {
  input.push(answer.trim());
}).on('close', () => {
  console.log(solution(input));
});
