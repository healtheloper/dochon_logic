function solution(s) {
  return [...s].every((v) => !isNaN(+v)) && (s.length === 6 || s.length === 4);
}
