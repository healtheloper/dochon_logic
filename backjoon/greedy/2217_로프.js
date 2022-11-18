const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const input = [];

const solution = (input) => {
  const [N, ...ropes] = input;

  let answer = 0;

  const ropeList = ropes.map((v) => +v).sort((a, b) => b - a);

  for (let i = 0; i < +N; i++) {
    ropeList.splice(+N - i, 1);
    answer = Math.max(answer, ropeList[ropeList.length - 1] * ropeList.length);
  }

  return answer;
};

rl.on('line', (answer) => {
  input.push(answer.trim());
}).on('close', () => {
  console.log(solution(input));
});
