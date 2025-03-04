const coordinateDisplay = document.getElementById('coordinate-display');



coordinateDisplay.addEventListener('click', function(event) {

  const x = event.clientX;

  const y = event.clientY;

  const coords = {x:x,y:y};




  const data = { key1: 'value1', key2: 'value2' };
  fetch('/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(coords)
  });

  setTimeout(function() {
    window.location.replace("/");
    console.log("This message appears after 1 second.");
  }, 500); // 1000 milliseconds = 1 second
  
  /*coordinateDisplay.textContent = `X: ${x}, Y: ${y}`;*/

});
