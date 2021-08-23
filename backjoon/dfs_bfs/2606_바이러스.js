const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const input = [];

const solution = (input) => {
  let answer = 0;
  const [node, edge, ...rest] = input;
  const graph = new Array(+node + 1).fill(null).map((v) => new Array());
  let queue = [];
  const visited = new Array(+node + 1).fill(null).map((v) => false);
  for (let i = 0; i < edge; i++) {
    const [from, to] = rest[i].split(" ");
    graph[from].push(to);
    graph[to].push(from);
  }
  visited[1] = true;
  queue.push(1);
  while (queue.length > 0) {
    const shiftNode = queue.shift();
    graph[shiftNode]?.forEach((v) => {
      if (!visited[+v]) {
        answer += 1;
        visited[+v] = true;
        queue.push(v);
      }
    });
  }
  return answer;
};

rl.on("line", (answer) => {
  input.push(answer.trim());
}).on("close", () => {
  console.log(solution(input));
});
