const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const input = [];

const solution = (input) => {
  const [t, ...rest] = input;
  const answer = rest.map((testCase) => {
    const [a, b] = testCase.split(" ");
    let lastA = 1;
    for (let i = 1; i <= b; i++) {
      lastA *= a;
      lastA %= 10;
    }
    return lastA === 0 ? 10 : lastA;
  });
  return answer.join("\n");
};

rl.on("line", (answer) => {
  input.push(answer.trim());
}).on("close", () => {
  console.log(solution(input));
});
