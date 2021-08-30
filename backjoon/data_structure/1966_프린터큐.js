const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const input = [];

const solution = (input) => {
  const [count, ...rest] = input;
  const result = [];
  for (let i = 0; i < count; i++) {
    const [n, m] = rest[2 * i].split(" ");
    const priority = rest[2 * i + 1].split(" ");
    const bigger = [...priority].sort((a, b) => +b - +a);
    const priority_q = priority.map((v, i) => [v, i]);
    let counts = 1;
    while (priority_q.length > 0) {
      const v = priority_q.shift();
      if (bigger[0] == v[0]) {
        if (v[1] == m) {
          result.push(counts);
          break;
        }
        bigger.shift();
        counts++;
      } else {
        priority_q.push(v);
      }
    }
  }
  return result.join("\n");
};

rl.on("line", (answer) => {
  input.push(answer.trim());
}).on("close", () => {
  console.log(solution(input));
});
