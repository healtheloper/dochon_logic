function solution(a, b) {
  return Array(Math.abs(a - b) + 1)
    .fill(0)
    .reduce((acc, _, idx) => acc + idx + Math.min(a, b), 0);
}
