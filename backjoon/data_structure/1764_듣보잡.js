const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const input = [];

const solution = (input) => {
  let answer = 0;
  const [count, ...rest] = input;
  const [n, m] = count.split(" ");
  let noListen = [];
  let noLook = [];
  rest.forEach((v, i) => {
    if (i < n) {
      noListen.push(v);
    } else {
      noLook.push(v);
    }
  });
  noListen = new Set([...noListen]);
  answer = noLook.filter((v) => noListen.has(v));
  answer.sort();
  return answer.length + "\n" + answer.join("\n");
};

rl.on("line", (answer) => {
  input.push(answer.trim());
}).on("close", () => {
  console.log(solution(input));
});
