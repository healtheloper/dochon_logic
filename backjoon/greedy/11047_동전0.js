const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const input = [];

const solution = (input) => {
  const [NK, ...coins] = input;
  let [N, K] = NK.split(' ').map((v) => +v);
  const coinList = coins.map((v) => +v).sort((a, b) => b - a);

  let answer = 0;
  coinList.forEach((coin) => {
    while (K >= coin) {
      K -= coin;
      answer += 1;
    }
  });

  return answer;
};

rl.on('line', (answer) => {
  input.push(answer.trim());
}).on('close', () => {
  console.log(solution(input));
});
