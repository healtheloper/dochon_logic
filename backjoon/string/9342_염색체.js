const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const input = [];
const startWord = ["A", "B", "C", "D", "E", "F"];

const isStartWith = (char) => {
  return startWord.includes(char);
};
const solution = (input) => {
  const [count, ...rest] = input;
  const answer = rest.map((string) => {
    const restString = string.split("");
    if (!isStartWith(restString[0])) return "Good";
    const firstA = restString.findIndex((char) => char == "A");
    const firstF = restString.findIndex((char) => char == "F");
    const firstC = restString.findIndex((char) => char == "C");
    const lastC = restString.lastIndexOf("C");
    if (firstA > firstF || firstF > firstC || firstA > firstC) return "Good";
    const lastString = restString.slice(lastC, restString.length);
    if (lastString.length > 1) return "Good";
    else if (lastString.length == 0) return "Infected!";

    if (!startWord.includes(lastString[0])) return "Good";
    return "Infected!";
  });
  return answer.join("\n");
};

rl.on("line", (answer) => {
  input.push(answer.trim());
}).on("close", () => {
  console.log(solution(input));
});
