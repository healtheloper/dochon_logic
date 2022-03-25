function solution(arr) {
  const answer = [];
  for (let i = 0; i < arr.length - 1; i++) {
    if (arr[i] === arr[i + 1]) continue;
    answer.push(arr[i]);
  }
  return [...answer, arr[arr.length - 1]];
}
