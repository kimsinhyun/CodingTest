function solution(n, left, right) {
  for (let i = left; i <= right; i++) {
    const t = Math.floor(i / n) + 1;
    if ((i % n) + 1 - t <= 0) {
      answer.push(t);
    } else {
      const a = (i % n) + 1 - t;
      answer.push(t + a);
    }
  }
  return answer;
}
