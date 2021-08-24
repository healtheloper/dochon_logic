const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const input = [];

const solution = (input) => {
  const [count, ...rest] = input;
  let dict = rest.map((r) => {
    const [x, y] = r.split(" ");
    return {
      x,
      y,
    };
  });
  dict = dict.sort((a, b) => {
    if (a.x === b.x) return a.y - b.y;
    return a.x - b.x;
  });
  dict = dict.map((position) => position.x + " " + position.y);
  return dict.reduce((prev, next) => prev + "\n" + next);
};

rl.on("line", (answer) => {
  input.push(answer.trim());
}).on("close", () => {
  console.log(solution(input));
});
