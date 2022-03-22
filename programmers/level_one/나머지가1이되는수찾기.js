function solution(n) {
  return Array(n)
    .fill(0)
    .map((_, i) => i + 1)
    .find((v) => n % v === 1);
}
