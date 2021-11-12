const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const input = [];

const solution = (input) => {
  const [n, m, ...infos] = input;
  const array = new Array(+n)
    .fill(null)
    .map((v) => new Array(+n).fill(Infinity));
  infos.forEach((info) => {
    const [a, b, c] = info.split(" ");
    array[+a - 1][+b - 1] = Math.min(array[+a - 1][+b - 1], +c);
  });
  for (let i = 0; i < +n; i++) {
    for (let j = 0; j < +n; j++) {
      for (let k = 0; k < +n; k++) {
        if (j == k) array[j][k] = 0;
        array[j][k] = Math.min(array[j][k], array[j][i] + array[i][k]);
      }
    }
  }
  return array
    .map((v) => {
      const tempV = v.map((item) => (item === Infinity ? 0 : item));
      return tempV.join(" ");
    })
    .join("\n");
};

rl.on("line", (answer) => {
  input.push(answer.trim());
}).on("close", () => {
  console.log(solution(input));
});
