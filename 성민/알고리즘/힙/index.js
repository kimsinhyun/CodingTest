/*
힙이란?
이진 트리 형태를 가지며 우선순위가 높은 요소가 먼저 나가기 위해 요소가 삽입, 
삭제 될 때 바로 정렬되는 특징이 있다.
*/

//MaxHeap
class MaxHeap {
  constructor() {
    this.heap = [null];
  }

  push(newValue) {
    this.heap.push(newValue);
    let currIndex = this.heap.length - 1;
    let parentIndex = Math.floor(currIndex / 2);
    while (currIndex !== 0 && newValue > this.heap[parentIndex]) {
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
      if (this.heap[rightIndex] < this.heap[leftIndex]) {
        const temp = this.heap[leftIndex];
        this.heap[leftIndex] = this.heap[currIndex];
        this.heap[currIndex] = temp;
        currIndex = leftIndex;
      } else {
        const temp = this.heap[rightIndex];
        this.heap[rightIndex] = this.heap[currIndex];
        this.heap[currIndex] = temp;
        currIndex = rightIndex;
      }
      leftIndex = currIndex * 2;
      rightIndex = currIndex * 2 + 1;
    }
    return value;
  }
}
