const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

// 0의 개수는 2 x 5 의 개수로 정해진다.
// 2 의 갯수는 항상 5의 갯수보다 많으므로 5의 갯수를 확인해 0의 갯수를 더한다.
const solution = (input) => {
  let answer = 0;
  for (let i = 0; i <= input; i++) {
    if (i % 5 == 0) {
      let temp = i;
      while (temp >= 5 && temp % 5 == 0) {
        temp /= 5;
        answer += 1;
      }
    }
  }
  return answer;
};

rl.on("line", (answer) => {
  console.log(solution(answer));
  rl.close();
});
