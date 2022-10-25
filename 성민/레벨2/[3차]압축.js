function solution(msg) {
  const answer = [];
  const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  const DICTIONARY = new Map();
  for (let i = 0; i < alphabet.length; i++) {
    DICTIONARY.set(alphabet[i], alphabet.charCodeAt(i) - 64);
  }
  let lastNum = 26;
  let index = 0;
  while (index < msg.length) {
    let temp = index;
    let word = msg[index];
    while (DICTIONARY.has(word) && temp < msg.length) {
      if (DICTIONARY.has(word)) index++;
      temp += 1;
      if (temp < msg.length) {
        word += msg[temp];
      }
    }
    if (DICTIONARY.has(word)) {
      answer.push(DICTIONARY.get(word));
    } else {
      lastNum++;
      answer.push(DICTIONARY.get(word.slice(0, word.length - 1)));
      DICTIONARY.set(word, lastNum);
    }
  }
  return answer;
}

console.log(solution("TOBEORNOTTOBEORTOBEORNOT"));
