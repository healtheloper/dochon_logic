// 1차 2번
// 정답률 55.57 %

function solution(N, stages) {
  const notClearInfo = {};
  let infos = [...stages];
  for (let i = 1; i <= N; i++) {
    const notClear = infos.filter((info) => info === i).length;
    notClearInfo[i] = notClear / infos.length;
    infos = infos.filter((info) => info !== i);
  }
  const sortedNotClearInfo = Object.entries(notClearInfo)
    .sort((o1, o2) => o2[1] - o1[1])
    .map((v) => +v[0]);

  return sortedNotClearInfo;
}
