function solution(x, n) {
  return Array(n)
    .fill(0)
    .map((_, i) => (i + 1) * x);
}
