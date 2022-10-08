function solution(lottos, win_nums) {
  const rank = {
    6: 1,
    5: 2,
    4: 3,
    3: 4,
    2: 5,
    1: 6,
    0: 6,
  };
  const rest_win_nums = win_nums;
  let zero_cnt = 0;
  let corret_cnt = 0;
  for (const lotto of lottos) {
    if (lotto === 0) {
      zero_cnt++;
      continue;
    }
    const index = rest_win_nums.indexOf(lotto);
    if (index !== -1) {
      rest_win_nums[index] = 50;
      corret_cnt++;
    }
  }
  return [rank[corret_cnt + zero_cnt], rank[corret_cnt]];
}
