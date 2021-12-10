// ! for not
if (!localStorage.getItem('counter')) {
  localStorage.setItem('counter', 0);
  // if not already a value for counter, set it to 0;
}

function count() {
    let counter = localStorage.getItem('counter');
    counter++;

    document.querySelector('h1').innerHTML = counter;

    // if (counter % 10 === 0) {
    //     alert(`Count is now ${counter}`)
    // }
    localStorage.setItem('counter', counter);
}
// DOMContentLoaded refers to the page being loaded
document.addEventListener('DOMContentLoaded', function() {
    // Anonymous function as argument of addEventListener
    document.querySelector('h1').innerHTML = localStorage.getItem('counter');
    document.querySelector('button').onclick = count;

    // setInterval(count, 1000);
    // increment every second
});
