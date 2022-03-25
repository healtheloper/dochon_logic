const 최소공배수얻기 = (n, m) => {
  let 최소공배수 = 1e9;
  for (let i = Math.min(n, m); i <= n * m; i++) {
    if (i % n === 0 && i % m === 0) {
      최소공배수 = Math.min(최소공배수, i);
    }
  }
  return 최소공배수;
};

const 최대공약수얻기 = (n, m) => {
  let 최대공약수 = -1;
  for (let i = 1; i <= Math.max(n, m); i++) {
    if (n % i === 0 && m % i === 0) {
      최대공약수 = Math.max(최대공약수, i);
    }
  }
  return 최대공약수;
};

function solution(n, m) {
  return [최대공약수얻기(n, m), 최소공배수얻기(n, m)];
}
