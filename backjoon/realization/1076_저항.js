const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const input = [];

const solution = (input) => {
  const colorDict = {
    black: {
      value: 0,
      mul: 1,
    },
    brown: {
      value: 1,
      mul: 10,
    },
    red: {
      value: 2,
      mul: 100,
    },
    orange: {
      value: 3,
      mul: 1_000,
    },
    yellow: {
      value: 4,
      mul: 10_000,
    },
    green: {
      value: 5,
      mul: 100_000,
    },
    blue: {
      value: 6,
      mul: 1_000_000,
    },
    violet: {
      value: 7,
      mul: 10_000_000,
    },
    grey: {
      value: 8,
      mul: 100_000_000,
    },
    white: {
      value: 9,
      mul: 1_000_000_000,
    },
  };
  const [first, second, third] = input;
  return (
    +(colorDict[first].value + "" + colorDict[second].value + "") *
    +colorDict[third].mul
  );
};

rl.on("line", (answer) => {
  input.push(answer.trim());
}).on("close", () => {
  console.log(solution(input));
});
