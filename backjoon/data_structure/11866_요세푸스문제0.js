const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = (input) => {
  const [n, k] = input.split(" ").map((v) => +v);
  const arr = new Array(n).fill(null).map((v, i) => i + 1);
  const result = [];
  let idx = k - 1;
  while (arr.length > 0) {
    const r = arr.splice(idx, 1)[0];
    idx += k - 1;
    if (idx >= arr.length) {
      idx %= arr.length;
    }
    result.push(r);
  }
  return "<" + result.join(", ") + ">";
};

rl.on("line", (answer) => {
  console.log(solution(answer));
  rl.close();
});
