function getBinaryArr(n, arr) {
  const result = [];
  for (let i = 0; i < n; i++) {
    let binaryArr = arr[i].toString(2);
    binaryArr =
      Array(n - binaryArr.length)
        .fill(0)
        .join("") + binaryArr;
    result.push(binaryArr.split(""));
  }
  return result;
}
function solution(n, arr1, arr2) {
  let answer = [];
  const binaryMap1 = getBinaryArr(n, arr1);
  const binaryMap2 = getBinaryArr(n, arr2);
  for (let i = 0; i < n; i++) {
    let result = "";
    for (let j = 0; j < n; j++) {
      if (binaryMap1[i][j] === "1" || binaryMap2[i][j] === "1") {
        result += "#";
      } else {
        result += " ";
      }
    }
    answer.push(result);
  }
  return answer;
}
