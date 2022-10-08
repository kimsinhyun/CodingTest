function solution(s) {
  const answer = [];
  for (const a of s.split("")) {
    if (a === "(") answer.push(a);
    else {
      if (answer.length === 0) return false;
      answer.pop();
    }
  }
  return answer.length > 0 ? false : true;
}
