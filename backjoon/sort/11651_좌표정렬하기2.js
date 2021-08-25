const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const input = [];

const solution = (input) => {
  const [count, ...positions] = input;
  let dicts = positions.map((position) => {
    const [x, y] = position.split(" ");
    return { x, y };
  });
  dicts.sort((a, b) => {
    if (a.y === b.y) {
      return a.x - b.x;
    }
    return a.y - b.y;
  });
  dicts = dicts.map((dict) => dict.x + " " + dict.y);
  return dicts.reduce((a, b) => a + "\n" + b);
};

rl.on("line", (answer) => {
  input.push(answer.trim());
}).on("close", () => {
  console.log(solution(input));
});
