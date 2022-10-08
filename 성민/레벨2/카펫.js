function solution(brown, yellow) {
  var answer = [];
  for (let i = 1; i <= yellow; i++) {
    if ((2 * yellow) / i + 4 + 2 * i === brown) {
      const a = i + 2;
      const b = (yellow + brown) / (i + 2);
      return a > b ? [a, b] : [b, a];
    }
  }
  return answer;
}

console.log(solution(10, 2));
