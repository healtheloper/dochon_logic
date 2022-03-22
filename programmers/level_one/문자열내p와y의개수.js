function solution(s) {
  let pCount = 0;
  let yCount = 0;

  [...s].forEach((c) => {
    if (c.toLowerCase() === "p") {
      pCount += 1;
    } else if (c.toLowerCase() === "y") {
      yCount += 1;
    }
  });
  return pCount === yCount;
}
