function sum(a) {
  let currentSum = a;

  function f(b) {
    currentSum += b;
    return f;
  }

  f.toString = function () {
    return currentSum;
  };
  f.valueOf = function () {
    return currentSum;
  };

  return f;
}

console.log(String(sum(1)(2))); // 3
console.log(String(sum(5)(-1)(2))); // 6
console.log(String(sum(6)(-1)(-2)(-3))); // 0
console.log(String(sum(0)(1)(2)(3)(4)(5))); // 15
