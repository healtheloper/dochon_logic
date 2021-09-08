const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const input = [];

const solution = (input) => {
  const [count, ...rest] = input;
  const answer = rest.map((arr) => {
    const [x1, y1, r1, x2, y2, r2] = arr.split(" ").map((v) => +v);
    const distance = (x2 - x1) ** 2 + (y2 - y1) ** 2;
    const plus = (r1 + r2) ** 2;
    const diff = (r1 - r2) ** 2;
    if (distance == 0 && diff == 0) return -1;
    if (distance == plus || distance == diff) return 1;
    else if (
      distance > plus ||
      distance < diff ||
      (distance == 0 && diff !== 0)
    )
      return 0;
    else if (distance < plus) return 2;
  });
  return answer.join("\n");
};

rl.on("line", (answer) => {
  input.push(answer.trim());
}).on("close", () => {
  console.log(solution(input));
});
