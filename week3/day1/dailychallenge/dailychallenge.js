let systems = ["terre", "mars", "pluton", "venus", "jupiter","uranus", "saturne", "neptune"]
let section = document.querySelector(".listPlanets")
for (let i of systems){
    let newDiv = document.createElement('div')
    let newTextNode = document.createTextNode(i);
    newDiv.appendChild(newTextNode);
    newDiv.classList.add("planet")
    section.appendChild(newDiv)
}