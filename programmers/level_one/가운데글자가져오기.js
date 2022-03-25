function solution(s) {
  return s.length % 2 === 1
    ? [...s].splice(s.length / 2, 1).join("")
    : [...s].splice(s.length / 2 - 1, 2).join("");
}
