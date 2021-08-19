const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = (input) => {
  let answer = 0;
  for (let i = 1; i <= input; i++) {
    let temp = 0;
    for (let j = i; j <= input; j++) {
      temp += j;
      if (temp > input) {
        break;
      } else if (temp == input) {
        answer += 1;
        break;
      }
    }
  }
  return answer;
};

rl.on("line", (answer) => {
  console.log(solution(answer));
  rl.close();
});
