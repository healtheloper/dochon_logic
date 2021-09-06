const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const input = [];

const solution = (input) => {
  const [n, m] = input[0].split(" ").map((v) => +v);
  const result = [];
  const visited = [];
  let output = "";
  const dfs = (cnt) => {
    if (cnt === m) {
      output += `${result.join(" ")}\n`;
      return;
    }
    for (let i = 0; i < n; i++) {
      if (visited[i] == true) continue;
      visited[i] = true;
      result.push(i + 1);
      dfs(cnt + 1);
      result.pop();
      visited[i] = false;
    }
  };
  dfs(0);
  return output;
};

rl.on("line", (answer) => {
  input.push(answer.trim());
}).on("close", () => {
  console.log(solution(input));
});
