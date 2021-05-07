function solution(array, commands) {
  var answer = [];
  for (const item of commands) {
    const i = item[0];
    const j = item[1];
    const k = item[2];
    let slice_array = array.slice(i - 1, j);
    slice_array.sort((a, b) => a - b);
    answer.push(slice_array[k - 1]);
  }
  return answer;
}
