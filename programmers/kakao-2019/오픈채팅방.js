// 1차 1번
// 정답률 59.91%

function solution(records) {
  const messages = [];
  const users = {};
  records.forEach((record) => {
    const [command, uid, name] = record.split(" ");
    if (command === "Enter") {
      users[uid] = name;
      messages.push([uid, "님이 들어왔습니다."]);
    } else if (command === "Leave") {
      messages.push([uid, "님이 나갔습니다."]);
    } else if (command === "Change") {
      users[uid] = name;
    }
  });
  return messages.map((message) => {
    const [uid, messageData] = message;
    return users[uid] + messageData;
  });
}
