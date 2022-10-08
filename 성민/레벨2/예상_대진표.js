function isFinish(a, b) {
  if (a % 2 === 0 && b % 2 === 1) return a - 1 === b;
  else if (b % 2 === 0 && a % 2 === 1) return b - 1 === a;
  return false;
}

function solution(n, a, b) {
  let count = 0;
  while (!isFinish(a, b)) {
    a = a % 2 === 0 ? a / 2 : (a + 1) / 2;
    b = b % 2 === 0 ? b / 2 : (b + 1) / 2;
    count++;
  }
  return count + 1;
}
// 예외 케이스
console.log(solution(8, 4, 5));
