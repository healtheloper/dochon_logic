function solution(arr) {
  let min = 1e9;
  arr.forEach((v) => {
    if (v < min) {
      min = v;
    }
  });
  return arr.length === 1 ? [-1] : arr.filter((v) => v !== min);
}
