const getMeasure = (n) => {
  const arr = [];
  for (let i = 1; i <= n; i++) {
    if (n % i === 0) {
      arr.push(i);
    }
  }
  return arr;
};

function solution(n) {
  if (n === 0) return 0;
  return getMeasure(n).reduce((a, b) => a + b);
}
