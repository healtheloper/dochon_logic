const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const input = [];

const solution = (input) => {
  const result = [];
  const [count, ...rest] = input;
  rest.forEach((v) => {
    if (v != 0) {
      result.push(v);
    } else {
      result.pop();
    }
  });
  if (result.length > 0) {
    return result.reduce((a, b) => +a + +b);
  } else {
    return 0;
  }
};

rl.on("line", (answer) => {
  input.push(answer.trim());
}).on("close", () => {
  console.log(solution(input));
});
