class MaxHeap {
  constructor() {
    this.heap = [null];
  }

  peek() {
    if (this.heap.length > 1) return this.heap[1];
    else return 0;
  }
  push(newValue) {
    this.heap.push(newValue);
    let currIndex = this.heap.length - 1;
    let parentIndex = Math.floor(currIndex / 2);
    while (parentIndex !== 0 && newValue > this.heap[parentIndex]) {
      const temp = this.heap[currIndex];
      this.heap[currIndex] = this.heap[parentIndex];
      this.heap[parentIndex] = temp;
      currIndex = parentIndex;
      parentIndex = Math.floor(currIndex / 2);
    }
  }

  pop() {
    const value = this.heap[1];
    this.heap[1] = this.heap.pop();
    let currIndex = 1;
    let leftIndex = 2;
    let rightIndex = 3;
    while (
      this.heap[currIndex] < this.heap[leftIndex] ||
      this.heap[currIndex] < this.heap[rightIndex]
    ) {
      if (this.heap[rightIndex] > this.heap[leftIndex]) {
        const temp = this.heap[rightIndex];
        this.heap[rightIndex] = this.heap[currIndex];
        this.heap[currIndex] = temp;
        currIndex = rightIndex;
      } else {
        const temp = this.heap[leftIndex];
        this.heap[leftIndex] = this.heap[currIndex];
        this.heap[currIndex] = temp;
        currIndex = leftIndex;
      }
      leftIndex = currIndex * 2;
      rightIndex = currIndex * 2 + 1;
    }
    return value;
  }
}

function solution(n, works) {
  const maxHeap = new MaxHeap();
  works.forEach((work) => maxHeap.push(work));

  while (n > 0 && maxHeap.peek() > 0) {
    n--;
    const maxValue = maxHeap.pop();
    maxHeap.push(maxValue - 1);
  }
  return maxHeap.heap.slice(1).reduce((pre, cur) => pre + cur * cur, 0);
}

console.log(solution(4, [4, 3, 3]));
