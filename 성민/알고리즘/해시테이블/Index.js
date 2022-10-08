// Map을 이용한 hash table 구현
const table = new Map();
table.set("key", 100);
table.set("key2", "Hello");
console.log(table["key"]); // undefined
console.log(table.get("key")); // 100
const object = { a: 1 };
table.set(object, "A1"); //Map 은 객체도 키로 사용가능함
console.log(table.get(object)); //A1

for (const a of table) {
  console.log(a);
}

table.delete(object);
table.set("key", 101); // 같은값 넣으면 덮어버림
console.log(table.get(object)); // undefined
console.log(table.keys()); // {'key','key3'}
console.log(table.values()); // {101, 'Hello'}
table.clear();
console.log(table.values()); // {}

// Set을 이용한 hash table 구현
const setTable = new Set();
setTable.add("key");
setTable.add("key2");
console.log(setTable.has("key")); // true
console.log(setTable.has("key3")); // false
setTable.delete("key");
console.log(setTable.has("key")); // false
console.log(setTable.size); //1
setTable.clear();
console.log(table.size); // 0
