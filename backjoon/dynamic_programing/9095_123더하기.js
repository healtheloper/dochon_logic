const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const input = [];

const solution = (input) => {
  const [N, ...cases] = input;

  const array = new Array(12).fill(0);
  array[1] = 1;
  array[2] = 2;
  array[3] = 4;

  for (let i = 4; i < 12; i++) {
    array[i] = array[i - 1] + array[i - 2] + array[i - 3];
  }
  return cases.map((v) => array[+v]).join('\n');
};

rl.on('line', (answer) => {
  input.push(answer.trim());
}).on('close', () => {
  console.log(solution(input));
});
