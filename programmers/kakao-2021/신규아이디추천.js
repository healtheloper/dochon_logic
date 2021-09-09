const step_one = (string) => string.toLowerCase();
const step_two = (string) => {
  const stringArr = string.split("");
  return stringArr.filter((char) => char.match(/[a-z0-9\.\-\_]/)).join("");
};
const step_three = (string) => {
  const stringArr = string.split("");
  return stringArr.reduce((a, b) => {
    if (a[a.length - 1] === b && b === ".") {
      return a;
    } else {
      return a + b;
    }
  });
};
const step_four = (string) => {
  let stringArr = string.split("");
  if (stringArr[0] === ".") stringArr = stringArr.slice(1, stringArr.length);
  if (stringArr[stringArr.length - 1] === ".")
    stringArr = stringArr.slice(0, stringArr.length - 1);
  return stringArr.join("");
};
const step_five = (string) => (string === "" ? "a" : string);
const step_six = (string) =>
  string.length > 15 ? step_four(string.slice(0, 15)) : string;
const step_seven = (string) =>
  string.length < 3
    ? string + string[string.length - 1].repeat(3 - string.length)
    : string;

function solution(new_id) {
  let answer = step_one(new_id);
  answer = step_two(answer);
  answer = step_three(answer);
  answer = step_four(answer);
  answer = step_five(answer);
  answer = step_six(answer);
  answer = step_seven(answer);
  return answer;
}

console.log(solution("...!@BaT#*..y.abcdefghijklm"));
console.log(solution("z-+.^."));
console.log(solution("=.="));
console.log(solution("123_.def"));
console.log(solution("abcdefghijklmn.p"));
