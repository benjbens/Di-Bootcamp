

function welcomeUser () {
	let section = document.getElementById("container");
	let newDiv = document.createElement("div");
	newDiv.classList.add("box");
	let textDiv = document.createTextNode("The sales end in 10min !");
	newDiv.appendChild(textDiv);

	section.appendChild(newDiv);
}

setTimeout(welcomeUser, 5000);