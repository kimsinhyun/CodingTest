function solution(s) {
  let answer = [];
  for (const i of s) {
    if (answer.length === 0) {
      answer.push(i);
    } else {
      if (answer[answer.length - 1] === i) {
        answer.pop();
      } else {
        answer.push(i);
      }
    }
  }
  return answer.length > 0 ? 0 : 1;
}

console.log(solution("abccaeeaba"));
