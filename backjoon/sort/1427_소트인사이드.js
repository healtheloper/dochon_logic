const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = (input) => {
  const arr = input.split("").map((v) => +v);
  arr.sort((a, b) => b - a);
  return arr.join("");
};

rl.on("line", (answer) => {
  console.log(solution(answer));
  rl.close();
});
