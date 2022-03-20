// Exercice 1

let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
console.log(fruits)
fruits.shift();
console.log(fruits)
fruits.sort();
console.log(fruits)
fruits.push("kiwi")
console.log(fruits)
fruits.splice(0, 1)
console.log(fruits)
const reversed = fruits.reverse();
console.log(fruits);

// Exercice 2

let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
console.log(moreFruits[1][1][0])