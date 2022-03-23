// Exerice 1


function infoAboutMe (){
	let name ="Benjamin"; 
	let age =19;
	let hobbies ="computers";
	console.log(`My name is ${name} im ${age} years old and I like ${hobbies}`);

}

infoAboutMe ()

function infoAboutPerson(personName, personAge, personFavoriteColor){
	console.log(`you're name is ${personName} you are ${personAge} year's old and your favorite color is ${personFavoriteColor}`)
}
	infoAboutPerson('thomas',19, 'blue')


	let a="David"
	let b=45
	let c="blue"

	infoAboutPerson(a,b,c,)

	let d="Josh"
	let e=12
	let f="Yellow"

	infoAboutPerson(d,e.f)


	// Exerice 2

	// function calculateTip()

	// let calculateTip = prompt("what ios the amount of the bill?");



	// calculateTip()


	// Exercice 3 



	function isDivisible(){



		let sum=0



	for(let i = 0; i <= 500; i++){
		if (i %23==0){
			console.log(i)
			sum=sum+i
			console.log(sum)
		}
		

	}
}
	isDivisible()



// Exercice 4

let stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

let prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 


let shoppingList = ['"banana”, “orange”,“apple”'];




function myBill(){
	let total = 0;
	for(x of shoppingList){
		if(stock[x]>0){
		total += prices[x];
		
		}



	}
console.log(total)


}


myBill()






// Exercice 5


function changeEnough(itemPrice, amountOfChange){
    let wallet = 0
    let coins = [0.25, 0.1, 0.05, 0.1];
    for (let i = 0; i < amountOfChange.length; i++ ){
        wallet += Number(amountOfChange[i]) * Number(coins[i]);
    }
    if(wallet >= itemPrice){
        return true;
    }
    return false;
}
let c = changeEnough(4.25,[25, 20, 5, 0]);
console.log(c);


















