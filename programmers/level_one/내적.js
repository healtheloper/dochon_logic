function solution(a, b) {
  return a.reduce((acc, next, idx) => acc + next * b[idx], 0);
}
