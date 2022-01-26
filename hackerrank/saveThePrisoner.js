function saveThePrisoner(n, m, s) {
  // Write your code here
  const rest = m % n;
  return (s - 1 + rest) % n === 0 ? n : (s - 1 + rest) % n;
}
