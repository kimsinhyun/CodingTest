function solution(x, n) {
  const answer = [];
  let curr = x;
  for (let i = 0; i < n; i++) {
    if (i > 0) {
      curr += x;
    }
    answer.push(curr);
  }
  return answer;
}

console.log(Number.isInteger(Number("t")));
