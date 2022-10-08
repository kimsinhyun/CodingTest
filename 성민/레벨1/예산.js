function solution(d, budget) {
  let result = 0;
  let restCost = budget;
  const rd = d.sort((a, b) => a - b);
  let i = 0;
  while (restCost >= rd[i]) {
    restCost -= rd[i];
    i++;
    result++;
  }
  return result;
}
