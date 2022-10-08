function solution(s) {
  let removeCnt = 0;
  let zeroCnt = 0;
  let binS = s;
  while (binS.length > 1) {
    removeCnt++;
    let changeS = "";
    for (const n of binS.split("")) {
      if (n === "0") zeroCnt++;
      else {
        changeS += n;
      }
    }
    binS = changeS.length.toString(2);
  }
  return [removeCnt, zeroCnt];
}

solution("110010101001");

"110010101001".toString(10);
