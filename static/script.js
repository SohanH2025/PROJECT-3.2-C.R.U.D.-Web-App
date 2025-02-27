const myDiv = document.getElementById("square");



myDiv.addEventListener("click", function(event) {

  const clickX = event.clientX;

  const clickY = event.clientY;

  console.log("Clicked at X:", clickX, "Y:", clickY);

});
