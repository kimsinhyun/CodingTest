function solution(n, money) {
  var answer = 0;
  let dp = Array(n + 1).fill(0);
  dp[0] = 1;
  money.forEach((el) => {
    for (let i = el; i < n + 1; i++) {
      dp[i] += dp[i - el];
    }
  });
  answer = dp[n] % 1000000007;
  return answer;
}

solution(5, [1, 2, 5]);

// 5원 => 5원을 정했어 쓰자고 이 동전을 쓰자고 정했어 => 5-5 => 0원이라는애가 몇가지방법이 있을까?
// 3=> dp[3]
