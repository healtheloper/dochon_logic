function solution(s) {
  let answer = "";

  const nums = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
  ];
  let curString = "";

  for (let i = 0; i < s.length; i++) {
    const char = s[i];
    if (!isNaN(+char)) answer += char;
    else {
      curString += char;
    }
    if (nums.includes(curString)) {
      answer += nums.indexOf(curString);
      curString = "";
    }
  }

  return +answer;
}
