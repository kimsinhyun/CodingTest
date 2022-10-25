function isPrimeNumber(number) {
  if (number <= 1) {
    return false;
  }
  for (let i = 2; i <= Math.sqrt(number); i++) {
    if (number % i === 0) {
      return false;
    }
  }
  return true;
}

function solution(n, k) {
  let answer = 0;
  n.toString(k)
    .split("0")
    .map((item) => Number(item))
    .forEach((ele) => {
      if (isPrimeNumber(ele)) answer++;
    });
  return answer;
}

console.log(solution(110011, 10));
