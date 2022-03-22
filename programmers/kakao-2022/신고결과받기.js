function solution(id_list, report, k) {
  const user = {};
  id_list.forEach((id) => {
    user[id] = {
      report: new Set(),
      reportedBy: new Set(),
    };
  });

  report.forEach((r) => {
    const [u, rt] = r.split(" ");
    user[u].report.add(rt);
    user[rt].reportedBy.add(u);
  });

  const stopU = id_list.filter((id) => user[id].reportedBy.size >= k);
  const reportU = Object.values(user).map((v) => [...v.report]);
  return reportU.map((arr) => arr.filter((v) => stopU.includes(v)).length);
}
