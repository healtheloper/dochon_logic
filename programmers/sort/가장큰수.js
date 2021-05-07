function compare(a, b) {
  a = a.toString();
  b = b.toString();
  return b + a - (a + b);
}
function solution(numbers) {
  var answer = "";
  numbers.sort(compare);
  answer = numbers.join("");
  return answer[0] === "0" ? "0" : answer;
}
