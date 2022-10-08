function solution(sizes) {
  let answer = 0;
  sizes = sizes.map((size) => size.sort((a, b) => b - a));
  let groupA = sizes.map((size) => size[0]);
  let groupB = sizes.map((size) => size[1]);
  answer = Math.max(...groupA) * Math.max(...groupB);
  return answer;
}
