const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const input = [];

const solution = (input) => {
  let answer = 1e9;
  const [NS, nums] = input;
  const [N, S] = NS.split(' ').map((v) => +v);

  const numList = nums.split(' ').map((v) => +v);

  const total = numList.reduce((acc, cur) => acc + cur, 0);

  if (total < S) {
    return 0;
  }

  let restTotal = total;

  for (let i = 0; i < N; i++) {
    let sum = 0;
    let count = 0;
    if (restTotal < S) break;
    for (let j = i; j < N; j++) {
      sum += numList[j];
      count += 1;
      if (sum >= S) {
        answer = Math.min(answer, count);
        break;
      }
    }
    restTotal -= numList[i];
  }

  return answer;
};

rl.on('line', (answer) => {
  input.push(answer.trim());
}).on('close', () => {
  console.log(solution(input));
});
