const coordinateDisplay = document.getElementById('coordinate-display');



coordinateDisplay.addEventListener('click', function(event) {

  const x = event.clientX;

  const y = event.clientY;

  const coords = {x:x,y:y};




  const data = { key1: 'value1', key2: 'value2' };
  fetch('/data', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(coords)
  });
  window.location.replace("/");
  
  /*coordinateDisplay.textContent = `X: ${x}, Y: ${y}`;*/

});
