function solution(s) {
  const words = s.split(" ");
  return words
    .map((word) =>
      [...word]
        .map((char, idx) => {
          if (idx % 2 == 0) return char.toUpperCase();
          return char.toLowerCase();
        })
        .join("")
    )
    .join(" ");
}
