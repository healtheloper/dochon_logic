function solution(absolutes, signs) {
  return absolutes.reduce(
    (sum, next, idx) => sum + next * (signs[idx] ? 1 : -1),
    0
  );
}
