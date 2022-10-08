function solution(nums) {
  let result = Math.floor(nums.length / 2);
  const newNumsLen = [...new Set(nums)].length;
  return newNumsLen > result ? result : newNumsLen;
}
