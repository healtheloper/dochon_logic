const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const input = [];

const solution = (input) => {
  let answer = [];
  const [T, ...rest] = input;
  for (let i = 0; i < T; i++) {
    let min = 1e9;
    let max = -1;
    const idx = i * 2;
    const str = rest[idx];
    const str_dict = {};
    const k = +rest[idx + 1];
    for (let x = 0; x < str.length; x++) {
      if (str_dict[str[x]]) str_dict[str[x]]++;
      else str_dict[str[x]] = 1;
    }
    for (let j = 0; j < str.length; j++) {
      const char = str[j];
      if (str_dict[char] < k) continue;
      let charCount = 0;
      for (let z = j; z < str.length; z++) {
        const compareChar = str[z];
        if (char === compareChar) {
          charCount++;
          if (charCount === k) {
            min = Math.min(z - j + 1, min);
            max = Math.max(z - j + 1, max);
            break;
          }
        }
      }
    }
    if (min !== 1e9) {
      answer.push(`${min} ${max}`);
    } else {
      answer.push("-1");
    }
  }
  return answer.join("\n");
};

rl.on("line", (answer) => {
  input.push(answer.trim());
}).on("close", () => {
  console.log(solution(input));
});
