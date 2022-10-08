class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class Queue {
  constructor() {
    this.size = 0;
    this.tail = null;
    this.head = null;
  }

  enqueue(newValue) {
    const newNode = new Node(newValue);
    if (this.head === null) {
      this.head = this.tail = newNode;
    } else {
      this.tail.next = newNode;
      this.tail = newNode;
    }
    this.size++;
  }

  dequeue() {
    const value = this.head.value;
    this.head = this.head.next;
    this.size -= 1;
    return value;
  }

  peek() {
    return this.head.value;
  }
  qsize() {
    return this.size;
  }
}

function solution(priorities, location) {
  var answer = 0;
  const q = new Queue();
  for (let i = 0; i < priorities.length; i++) {
    q.enqueue([priorities[i], i]);
  }
  priorities.sort((a, b) => b - a);
  let cnt = 0;
  while (q.qsize() > 0) {
    const top = q.peek();
    if (top[0] === priorities[cnt]) {
      if (top[1] === location) return cnt + 1;
      else {
        q.dequeue();
        cnt++;
      }
    } else {
      q.dequeue();
      q.enqueue(top);
    }
  }
  return answer;
}

console.log(solution([1, 1, 9, 1, 1, 1], 0));
