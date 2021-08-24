const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = (input) => {
  const [a, b] = input.split(" ").map((v) => +v);
  let min = 0;
  for (let i = 0; i <= Math.max(a, b); i++) {
    if (a % i == 0 && b % i == 0) {
      min = Math.max(min, i);
    }
  }
  const max = parseInt(a / min) * parseInt(b / min) * min;
  return min + "\n" + max;
};

rl.on("line", (answer) => {
  console.log(solution(answer));
  rl.close();
});
