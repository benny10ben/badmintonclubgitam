// navigation background
function changeBg() {
    var navbar = document.getElementById('navbar')
    var scrollValue = window.scrollY;
    if(scrollValue < 150){
        navbar.classList.remove('bgColor');
    } else{
        navbar.classList.add('bgColor'); 
    }
}

window.addEventListener('scroll', changeBg);

// Main menu
function myFunction() {
    var x = document.getElementById("myLinks");
    if (x.style.display === "block") {
      x.style.display = "none";
    } else {
      x.style.display = "block";
    }
}


function myFunction2() {
    var x = document.getElementById("team");
    x.style.display = "none";
    var y = document.getElementById("alumni");
    y.style.display = "block";
}

function myFunction3() {
  var x = document.getElementById("team");
  x.style.display = "block";
  var y = document.getElementById("alumni");
  y.style.display = "none";
}


const lp1 = document.querySelector('.lp1');
const lp2 = document.querySelector('.lp2');
const lp3 = document.querySelector('.lp3');
const lp4 = document.querySelector('.lp4');
document.querySelector('.l1').addEventListener('mouseover', function() {
  lp1.style.opacity = 1;
});

document.querySelector('.l1').addEventListener('mouseout', function() {
  lp1.style.opacity = 0;
});


document.querySelector('.l2').addEventListener('mouseover', function() {
  lp2.style.opacity = 1;
});

document.querySelector('.l2').addEventListener('mouseout', function() {
  lp2.style.opacity = 0;
});



document.querySelector('.l3').addEventListener('mouseover', function() {
  lp3.style.opacity = 1;
});

document.querySelector('.l3').addEventListener('mouseout', function() {
  lp3.style.opacity = 0;
});



document.querySelector('.l4').addEventListener('mouseover', function() {
  lp4.style.opacity = 1;
});

document.querySelector('.l4').addEventListener('mouseout', function() {
  lp4.style.opacity = 0;
});

