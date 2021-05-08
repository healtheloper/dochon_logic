function graphs(words, start, graph) {
  for (const word of words) {
    let count = 0;
    let idx = 0;
    for (const char of word) {
      if (start[idx] === char) {
        count++;
      }
      idx++;
    }
    if (count == word.length - 1) {
      if (!graph[start].includes(word)) {
        graph[start].push(word);
      }
      if (!graph[word].includes(start)) {
        graph[word].push(start);
      }
    }
  }
}
function dfs(x, visited, dfsArray, graph, target) {
  if (dfsArray.includes(target)) {
    return;
  }
  if (graph[x].includes(target)) {
    dfsArray.push(target);
    return;
  }
  visited[x] = 1;
  dfsArray.push(x);
  for (const item of graph[x]) {
    if (visited[item] == 0) {
      dfs(item, visited, dfsArray, graph, target);
    }
  }
}
function solution(begin, target, words) {
  var answer = 0;
  let graph = {};
  let visited = {};
  const dfsArray = [];
  graph[begin] = [];
  for (const word of words) {
    graph[word] = [];
    visited[word] = 0;
  }
  graphs(words, begin, graph);
  for (const word of words) {
    graphs(words, word, graph);
  }
  dfs(begin, visited, dfsArray, graph, target);
  if (Object.values(visited).includes(0)) {
    answer = dfsArray.length;
  }
  return answer;
}
function graphs(words, start, graph) {
  for (const word of words) {
    let count = 0;
    let idx = 0;
    for (const char of word) {
      if (start[idx] === char) {
        count++;
      }
      idx++;
    }
    if (count == word.length - 1) {
      if (!graph[start].includes(word)) {
        graph[start].push(word);
      }
      if (!graph[word].includes(start)) {
        graph[word].push(start);
      }
    }
  }
}
function dfs(x, visited, dfsArray, graph, target) {
  if (dfsArray.includes(target)) {
    return;
  }
  if (graph[x].includes(target)) {
    dfsArray.push(target);
    return;
  }
  visited[x] = 1;
  dfsArray.push(x);
  for (const item of graph[x]) {
    if (visited[item] == 0) {
      dfs(item, visited, dfsArray, graph, target);
    }
  }
}
function solution(begin, target, words) {
  var answer = 0;
  let graph = {};
  let visited = {};
  const dfsArray = [];
  graph[begin] = [];
  for (const word of words) {
    graph[word] = [];
    visited[word] = 0;
  }
  graphs(words, begin, graph);
  for (const word of words) {
    graphs(words, word, graph);
  }
  dfs(begin, visited, dfsArray, graph, target);
  if (Object.values(visited).includes(0)) {
    answer = dfsArray.length;
  }
  return answer;
}
