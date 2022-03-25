function solution(s, n) {
  const upper = Array(26)
    .fill(0)
    .map((_, i) => String.fromCharCode(i + 65));
  const lower = Array(26)
    .fill(0)
    .map((_, i) => String.fromCharCode(i + 97));

  return [...s]
    .map((c) => {
      if (!upper.includes(c) && !lower.includes(c)) return c;
      const code = c.charCodeAt();
      if (code >= 91) {
        return lower[(code - 97 + n) % 26];
      }
      return upper[(code - 65 + n) % 26];
    })
    .join("");
}
