function solution(places) {
  const placesArr = places.map((place) => place.map((v) => v.split("")));
  const findP = (place) => {
    const p = [];
    place.forEach((row, rowIdx) => {
      row.forEach((value, colIdx) => {
        if (value == "P") p.push([rowIdx, colIdx]);
      });
    });
    return p;
  };
  const findDiff = (arr) => {
    const diffArr = [];
    arr.forEach((p1) => {
      arr.forEach((p2) => {
        const [x1, y1] = p1;
        const [x2, y2] = p2;
        const diff = Math.abs(x1 - x2) + Math.abs(y1 - y2);
        if (diff <= 2 && [x1, y1].join("") !== [x2, y2].join(""))
          diffArr.push([p1, p2]);
      });
    });
    return diffArr;
  };
  const isDiff = (diff, place) => {
    const [[x1, y1], [x2, y2]] = diff;
    if (x1 !== x2 && y1 !== y2)
      return place[x2][y1] == "X" && place[x1][y2] == "X";
    else if (x1 !== x2) return place[parseInt((x1 + x2) / 2)][y1] == "X";
    else if (y1 !== y2) return place[x1][parseInt((y1 + y2) / 2)] == "X";
  };
  return placesArr.map((place) => {
    const diffs = findDiff(findP(place));
    if (diffs.length == 0) return 1;
    return diffs.filter((diff) => !isDiff(diff, place)).length > 0 ? 0 : 1;
  });
}
