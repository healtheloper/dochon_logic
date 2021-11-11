const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const input = [];

const solution = (input) => {
  const [n, m] = input[0].split(" ").map((v) => +v);
  const array = input[1].split(" ");
  const result = [];
  const visited = [];
  let output = [];
  const dfs = (cnt) => {
    if (cnt === m) {
      output.push(result.join(" "));
      return;
    }
    for (let i = 0; i < n; i++) {
      if (visited[i] === true) continue;
      result.push(array[i]);
      visited[i] = true;
      dfs(cnt + 1);
      result.pop();
      visited[i] = false;
    }
  };
  dfs(0);
  output.sort((a, b) => {
    const aArr = a.split(" ");
    const bArr = b.split(" ");
    for (let i = 0; i < aArr.length; i++) {
      if (aArr[i] === bArr[i]) continue;
      return +aArr[i] - +bArr[i];
    }
  });
  return output.join("\n");
};

rl.on("line", (answer) => {
  input.push(answer.trim());
}).on("close", () => {
  console.log(solution(input));
});
