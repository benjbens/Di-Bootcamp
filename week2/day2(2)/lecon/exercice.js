let userCart = {
	username : "John",
	password: 1234,
	isUserSignedIn : true,
	cart : {
		apple : 2,
		banana : 1,
		pear : 5,
	},
	prices : {
		apple : 0.5,
		banana : 0.8646466363,
		pear : 0.2
	}
};
console.log(userCart);


userCart ["lastname"] ="Smith"
console.log(userCart);

userCart ["prices"]["pear"] *=1.7
console.log(userCart);


let userFruits = prompt(" What fruit do you want: Apple, banana or pear")
let userFruitsLower = userFruits.toLowerCase();
console.log(userFruitsLower);


// console.log(userCart["prices"]["apple"]);
// console.log(userCart["prices"]["pear"]);
// console.log(userCart["prices"]["banana"]);

console.log(userCart["prices"][userFruits]);