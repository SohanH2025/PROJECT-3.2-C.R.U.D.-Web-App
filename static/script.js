const coordinateDisplay = document.getElementById('coordinate-display');



coordinateDisplay.addEventListener('click', function(event) {

  const x = event.clientX;

  const y = event.clientY;

  fetch('/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({x:x,y:y})
})
  /*coordinateDisplay.textContent = `X: ${x}, Y: ${y}`;*/

});
