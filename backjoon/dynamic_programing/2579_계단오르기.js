const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const input = [];

const solution = (input) => {
  const [N, ...stairs] = input;

  const array = new Array(+N + 1).fill(0);
  const stairList = stairs.map((v) => +v);

  array[1] = stairList[0];
  array[2] = stairList[0] + stairList[1];

  for (let i = 3; i < array.length; i++) {
    array[i] = Math.max(
      array[i - 2] + stairList[i - 1],
      array[i - 3] + stairList[i - 2] + stairList[i - 1]
    );
  }

  return array[+N];
};

rl.on('line', (answer) => {
  input.push(answer.trim());
}).on('close', () => {
  console.log(solution(input));
});
