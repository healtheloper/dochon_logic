const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = (input) => {
  let answer = 0;
  input.split(" ").forEach((v) => {
    answer += v ** 2;
  });
  return answer % 10;
};

rl.on("line", (answer) => {
  console.log(solution(answer));
  rl.close();
});
