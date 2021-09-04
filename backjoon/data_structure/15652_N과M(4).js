const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const input = [];

const solution = (input) => {
  const [n, m] = input[0].split(" ").map((v) => +v);
  const array = new Array(n).fill(null).map((v, i) => i + 1);
  const result = [];
  let output = "";
  const dfs = (idx, cnt) => {
    if (cnt === m) {
      output += `${result.join(" ")}\n`;
      return;
    }
    for (let i = idx; i < n; i++) {
      result.push(i + 1);
      dfs(i, result.length);
      result.pop();
    }
  };
  dfs(0, 0);
  return output;
};

rl.on("line", (answer) => {
  input.push(answer.trim());
}).on("close", () => {
  console.log(solution(input));
});
