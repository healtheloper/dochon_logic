function solution(bridge_length, weight, truck_weights) {
  let complete = [];
  let crossing = [];
  const trucks = [...truck_weights];
  let waitIdx = 0;
  let i = 0;
  while (true) {
    if (complete.length === truck_weights.length) return i;
    crossing.forEach((obj) => {
      obj.time++;
      if (obj.time >= bridge_length) complete.push(obj.weight);
    });
    crossing = crossing.filter((obj) => obj.time < bridge_length);
    const curCrossingWeight =
      crossing.length > 0
        ? crossing.map((v) => v.weight).reduce((a, b) => a + b)
        : 0;
    if (curCrossingWeight + trucks[waitIdx] <= weight) {
      crossing.push({ weight: trucks[waitIdx], time: 0 });
      waitIdx++;
    }
    i++;
  }
}
