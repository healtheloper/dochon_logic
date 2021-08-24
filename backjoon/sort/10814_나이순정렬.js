const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const input = [];

const solution = (input) => {
  let answer = 0;
  const [count, ...rest] = input;
  let userDict = rest.map((user, idx) => {
    const [age, name] = user.split(" ");
    return {
      id: idx,
      name,
      age,
    };
  });
  userDict = userDict.sort((a, b) => {
    return a.age - b.age;
  });
  userDict = userDict.map((user) => user.age + " " + user.name);
  return userDict.reduce((prev, next) => prev + "\n" + next);
};

rl.on("line", (answer) => {
  input.push(answer.trim());
}).on("close", () => {
  console.log(solution(input));
});
