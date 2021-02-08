(function ($) {

  'use strict'

  const scrollToTopButton = document.querySelector(".back-to-top");

function headerScroll() {
  // Get the current scroll value
  let Y = document.documentElement.scrollTop || document.body.scrollTop ;
  // If the scroll value is greater than the window height, let's add a class to the scroll-to-top button to show it!
  if (Y > 190) {
    scrollToTopButton.classList.add("show-toTop-btn");
  } else {
    scrollToTopButton.classList.remove("show-toTop-btn");
  }
}

//our scroll function that will be called when the scroll button is clicked
function scrollToTop() {
  //getting the currentPosition position of the button
  const currentPosition =
    document.body.scrollTop || document.documentElement.scrollTop;
  // If that number is greater than 0, we'll scroll back to 0, or the top of the document.
  // We'll also animate that scroll with requestAnimationFrame:
  // https://developer.mozilla.org/en-US/docs/Web/API/window/requestAnimationFrame
  if (currentPosition > 0) {
    //Animating the scroll with the javascript requestAnimationFrame function
    window.requestAnimationFrame(scrollToTop);
    window.scrollTo(0, currentPosition - currentPosition / 10);
  }
}

scrollToTopButton.addEventListener("click", (event) => {
  event.preventDefault();
  scrollToTop();
});


window.addEventListener("scroll", () => {
  headerScroll();
});

 // Initiate the wowjs animation library
 new WOW().init();

 document.querySelectorAll('.tooltip-demo')
 .forEach(tooltip => new bootstrap.Tooltip(tooltip, {
  selector: '[data-bs-toggle="tooltip"]'
}))

 document.querySelectorAll('[data-bs-toggle="popover"]')
 .forEach(popup => new bootstrap.Popover(popup))

 // Disable empty links
$('a[href="#"], a[href=""]').attr('href', 'javascript:void(0)');

// a dark Mode API
const toggleModeButton = document.getElementById("dark-mode-toggle");
const switchMode = document.getElementById("switch-theme");

const prefersDarkScheme = window.matchMedia("(prefers-color-scheme: dark)");

 //toggling our day and night icons
function changeIcon() {
    switchMode.classList.toggle("active");
}

function toggleTheme(event) {  
    event.preventDefault()
    let theme
    // check if dark mode is enabled
    if (prefersDarkScheme.matches) {
        document.body.classList.toggle("light-theme");
        theme = document.body.classList.contains("light-theme")
        ? "light"
        : "dark";
    }
    else {
        document.body.classList.toggle("dark-theme");
        theme = document.body.classList.contains("dark-theme") ? "dark" : "light";
      }
    // update the current theme and storing it to the localStorage
    localStorage.setItem('theme', theme)
    console.log(theme);
}

// EventListener for button to toggle btw dark and light mode 
toggleModeButton.addEventListener("click", (event) => {
    event.preventDefault();
    changeIcon()
    setTimeout(function() {
      toggleTheme(event)
    }, 500);
    console.log("Toggled!");
  });

// onload function to load the correct theme from the localStorage
window.addEventListener("load", () => {
  const currentTheme = localStorage.getItem("theme");
  if (currentTheme == "dark") {
    setTimeout(function() {
      document.body.classList.toggle("dark-theme");
    }, 500);
    changeIcon()
  }
  else if  (currentTheme == "light") {
    document.body.classList.toggle("light-theme");
  }
});

    //Mobile nav

    const mobile_nav = document.getElementById('mobile-nav'),
        openMobileNav = document.querySelector('.mobile-nav-toggle')
        
    openMobileNav.addEventListener('click', (e) => {
        e.preventDefault()
        mobile_nav.classList.toggle('mobile-nav-slide');
    });

})(jQuery)
