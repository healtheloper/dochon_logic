function solution(priorities, location) {
  let answer = 1;
  const priority = [...priorities].map((p, idx) => {
    return {
      value: p,
      idx,
    };
  });
  const prioritySort = priorities.sort((a, b) => a - b);
  while (priority.length > 0) {
    if (priority[0].value == prioritySort[prioritySort.length - 1]) {
      console.log(priority, prioritySort);
      const { idx } = priority.shift();
      prioritySort.pop();
      if (idx == location) {
        return answer;
      }
      answer++;
    } else {
      const p = priority.shift();
      priority.push(p);
    }
  }
}
