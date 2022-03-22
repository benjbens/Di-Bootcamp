// Exercice 1

let people = ["Greg", "Mary", "Devon", "James"]
people.shift(0, 1);
console.log(people)
people.splice(2, 1, "jason");
console.log(people)
people.push("Benjamin");
console.log(people)
console.log(people.indexOf("Mary"))
console.log(people.slice(1))

// because the word does not exist

let last = people [people.length-1];
console.log(last)
console.log(people)
for (let i = 0; i < people.length -1; i ++) {
	
	if (people[i] === "jason") { 
		break;
	} 
	console.log(people[i])
}


// Exercice 2


let colors =["bleu", "rouge", "orange", "vert"]

for (let i=0; i < colors.length; i ++) {
	console.log(colors[i])


}



// Exercice 3

let num=0;
while (num < 10){

num = prompt ("Pick a number")
console.log(num);

if(!isNaN && num > 10){

	}
}

// |Exercice 4

let building = {
    numberOfFloors : 4,
    numberOfAptByFloor : {
        firstFloor : 3,
        secondFloor : 4,
        thirdFloor : 9,
        fourthFloor : 2,
    },
    nameOfTenants : ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan :  [4, 1000],
        david : [1, 500],
    },

}

console.log(building.numberOfFloors)
console.log(building.numberOfAptByFloor.firstFloor)
console.log(building.numberOfAptByFloor.thirdFloor)
console.log(building.numberOfRoomsAndRent.dan)


// Exercice 5




// Exercice 6




let details = {
  my: 'name',
  is: 'Rudolf',
  the: 'raindeer'
}

for (x in details) {
	console.log([x])
  console.log(details[x])
}



// Exerice 7

let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
let arr = []
for (let i = 0; i < names.length; i++){
	let name =names[i];
	arr.push(name[0]);
}
	console.log(arr.sort().join(''))




