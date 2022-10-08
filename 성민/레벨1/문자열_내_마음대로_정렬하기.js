function solution(strings, n) {
  return strings.sort(function (a, b) {
    if (a[n] < b[n]) return -1;
    if (a[n] > b[n]) return 1;
    if (a[n] === b[n]) {
      if (a < b) return -1;
      else if (a === b) return 0;
      else return 1;
    }
  });
}
