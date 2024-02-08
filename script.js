const inputBox = document.getElementById("input-box");
const listContainer = document.getElementById("list-container");

function addTask(){
    if(inputBox.value === ''){
        alert("Vous devez écrire quelque chose !");
    
    }
    else{
        let li = document.createElement("li");
        li.innerHTML = inputBox.value;
        listContainer.appendChild(li);
        let span =  document.createElement("span"); /* Changer l'image quand on décoche */
        span.innerHTML = "\u00d7"; /* Ajoute une icône en croix */
        li.appendChild(span);
        }
        

    
    inputBox.value = "";  /* Remettre le champ vide */
    saveData();
}

listContainer.addEventListener("click", function(e){
    if(e.target.tagName === "LI"){
        e.target.classList.toggle("checked");
        saveData();
    }
    else if(e.target.tagName === "SPAN"){
        e.target.parentElement.remove();
        saveData();
    }
}, false)

function saveData(){
    localStorage.setItem("data", listContainer.innerHTML);

}
function showTask(){
    listContainer.innerHTML = localStorage.getItem("data");
}
showTask();