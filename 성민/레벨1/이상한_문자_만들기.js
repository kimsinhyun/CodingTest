function solution(s) {
  const words = s.split(" ");
  return words
    .map((word) => {
      let transWord = "";
      for (let i = 0; i < word.length; i++) {
        if (i % 2 === 0) transWord += word[i].toUpperCase();
        else transWord += word[i].toLowerCase();
      }
      return transWord;
    })
    .join(" ");
}
