const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const input = [];

const solution = (input) => {
  let answer = [];
  input.pop();
  const tokens = input.map((i) => i.split(""));
  const parenthesis = ["[", "]", "(", ")"];
  const open = ["[", "("];
  const arr = tokens.map((token) =>
    token.filter((t) => parenthesis.includes(t))
  );
  const stacks = [];
  for (let j = 0; j < arr.length; j++) {
    let element = arr[j];
    const stack = [];
    for (let i = 0; i < element.length; i++) {
      if (open.includes(element[i])) {
        stack.push(element[i]);
      } else {
        if (element[i] === "]" && stack[stack.length - 1] === "[") {
          stack.pop();
        } else if (element[i] === ")" && stack[stack.length - 1] === "(") {
          stack.pop();
        } else {
          arr[j] = "no";
          break;
        }
      }
    }
    stacks.push(stack);
  }
  answer = arr.map((el, idx) => {
    if (el !== "no") {
      if (stacks[idx].length === 0) {
        return "yes";
      } else {
        return "no";
      }
    } else {
      return el;
    }
  });
  return answer.join("\n");
};

rl.on("line", (answer) => {
  input.push(answer.trim());
}).on("close", () => {
  console.log(solution(input));
});
