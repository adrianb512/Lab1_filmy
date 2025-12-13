
function addmovie()
{
var li = document.createElement("li");
 var movieTitle = document.getElementById("inputTitle").value;
 var movieYear = document.getElementById("movieYear").value;
 var movieActors = document.getElementById("movieActors").value;

li.innerHTML = "<input type='checkbox'> " + movieTitle + ", " + movieYear + ", " + movieActors+"</input>";

if(movieTitle=="")
{
alert("movieTitle - Cannot be empty");

}else if(movieYear=="")
{
alert("movieYear-Cannot be empty");

}else if(movieActors=="")
{
alert("movieActors-Cannot be empty");

}else
{
document.getElementById("movielist").appendChild(li);
}

 var movieTitle = document.getElementById("inputTitle").value="";
 var movieYear = document.getElementById("movieYear").value="";
 var movieActors = document.getElementById("movieActors").value="";

}

function deletemovie()
{

var checkedBoxes = document.querySelectorAll("input[type='checkbox']:checked");
const j = checkedBoxes.length;

for(let i=0;i<=j;i++)
{
document.getElementById("movielist").removeChild(checkedBoxes[i].parentNode);
}


}