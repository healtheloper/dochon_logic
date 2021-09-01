const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split(/\s+/);

const solution = (input) => {
  const pokeMonCount = +input[0];
  const pokeMon = input.slice(2, pokeMonCount + 2);
  const answers = input.slice(pokeMonCount + 2);
  const pokeMonDict = {};
  pokeMon.forEach((v, i) => (pokeMonDict[v] = i + 1));
  return answers
    .map((a) => {
      if (Number.isNaN(+a)) {
        return pokeMonDict[a];
      } else {
        return pokeMon[+a - 1];
      }
    })
    .join("\n");
};

console.log(solution(input));
