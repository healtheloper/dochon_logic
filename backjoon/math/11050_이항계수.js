const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = (input) => {
  const [n, k] = input.split(" ").map((v) => +v);
  let parent = 1;
  let child = 1;
  for (let i = 0; i < k; i++) {
    parent *= n - i;
    child *= k - i;
  }
  return parseInt(parent / child);
};

rl.on("line", (answer) => {
  console.log(solution(answer));
  rl.close();
});
