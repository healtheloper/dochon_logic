const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const input = [];

const solution = (input) => {
  const [info, status, ...commands] = input;

  const array = status.split(" ").map((v) => +v);
  const active = {
    1: (l, x) => {
      array[l - 1] = +x;
    },
    2: (l, r) => {
      for (let i = l - 1; i < r; i++) {
        array[i] = +!array[i];
      }
    },
    3: (l, r) => {
      for (let i = l - 1; i < r; i++) {
        array[i] = 0;
      }
    },
    4: (l, r) => {
      for (let i = l - 1; i < r; i++) {
        array[i] = 1;
      }
    },
  };
  commands.forEach((com) => {
    const [c, l, r] = com.split(" ");
    active[c](l, r);
  });
  return array.join(" ");
};

rl.on("line", (answer) => {
  input.push(answer.trim());
}).on("close", () => {
  console.log(solution(input));
});
