let colors = ["blue", "yellow", "green", "pink"];


function createbutton() {
let container = document.getElementById("container");

	for (let i=0; i<colors.length; i++) {
		let button = document.createElement("button");
		button.textContent = colors[i];
		button.style.backgroundcolor = colors[i];
		button.addEventListener("click", changebackgroundcolor);
		container.appendChild(button);


	}
	
	
}


createbutton()


function changebackgroundcolor (evt){
	console.log(evt.target.style.backgroundcolor)
	document.body.style.backgroundcolor = evt.target.style.backgroundcolor;
}