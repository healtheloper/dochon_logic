const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const input = [];

const solution = (input) => {
  const [N, A, B] = input;
  const aList = A.split(' ')
    .map((v) => +v)
    .sort((a, b) => a - b);
  const bList = B.split(' ')
    .map((v) => +v)
    .sort((a, b) => b - a);

  return aList.reduce((acc, cur, idx) => acc + cur * bList[idx], 0);
};

rl.on('line', (answer) => {
  input.push(answer.trim());
}).on('close', () => {
  console.log(solution(input));
});
