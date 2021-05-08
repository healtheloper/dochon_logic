const solution = (tickets) => {
  let answer = [];
  const DFS = (airport, tickets, path) => {
    let newPath = [...path, airport];
    if (tickets.length == 0) {
      answer.push(newPath);
    } else {
      tickets.map((ticket, idx) => {
        if (ticket[0] === airport) {
          let copiedTickets = [...tickets];
          // idx 인 곳에 1개를 삭제 -> 삭제한 곳의 데이터
          const [[from, to]] = copiedTickets.splice(idx, 1);
          DFS(to, copiedTickets, newPath);
        }
      });
    }
  };
  DFS("ICN", tickets, []);
  console.log(answer);
  return answer.sort()[0];
};

solution([
  ["ICN", "JFK"],
  ["HND", "IAD"],
  ["JFK", "HND"],
]);

solution([
  ["ICN", "SFO"],
  ["ICN", "ATL"],
  ["SFO", "ATL"],
  ["ATL", "ICN"],
  ["ATL", "SFO"],
]);
