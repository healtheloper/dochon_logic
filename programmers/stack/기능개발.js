function solution(progresses, speeds) {
  var answer = [];
  let count = 0;
  let pro = [...progresses];
  let cursor = 0;
  while (count < speeds.length) {
    let temp_count = 0;
    for (let i = cursor; i < speeds.length; i++) {
      pro[i] += speeds[i];
    }
    if (pro[cursor] >= 100) {
      for (let i = cursor; i < pro.length; i++) {
        if (pro[i] >= 100) {
          temp_count += 1;
          if (count + temp_count == speeds.length) {
            count += temp_count;
            answer.push(temp_count);
            break;
          }
          continue;
        } else {
          cursor = i;
          count += temp_count;
          answer.push(temp_count);
          temp_count = 0;
          break;
        }
      }
    }
  }
  return answer;
}

console.log(solution([93, 30, 55], [1, 30, 5]));
