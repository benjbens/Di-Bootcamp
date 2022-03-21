// Exercice 1

let x = 5;
let y = 4;

if (x > y) { 
console.log(`${x} is the bigger number`)

}else{ 
console.log(`${y} is the bigger number`)
}

// Exercice 2

let newdog = "Chihuahua";
let number = newdog.length;
console.log(`the number is ${number}`);

console.log(newdog.toLowerCase());
console.log(newdog.toUpperCase());

if ( newdog == "Chihuahua") {
	console.log(`I love Chihuahuas, it’s my favorite dog breed`)

} else {
	console.log(`I dont care, I prefer cats`)
}

// Exrcice 3

let person = prompt("Pick a number");
person=Number(person)

 if (person % 2 == 0) {
 	console.log(`x is an even number`)

 } else {
 	console.log(`y is an odd number`)
 }

 // Exercice 4


let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
console.log(users)
let len = users.length;

if (len === 0) {
	console.log(`no one is online`);

} else if(len === 1){
	console.log(users[o] `is online`);

}else if(len === 2){
	console.log(users[1], user[2] `are online`);

}else if (len > 2) {
	console.log(users[0], users[1], `more ${len-2} are online`);
}






