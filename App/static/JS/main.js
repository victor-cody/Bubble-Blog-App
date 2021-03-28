import {
  Theme
} from "./theme.mjs";

(function ($, theme) {
  'use strict'

  function giveBodyMargin(header = "#header", main = "#main",  footer = "#footer", ) {
    if (!document.querySelector(header)) return;

    let margin = document.querySelector(header).getBoundingClientRect().left
    if (margin >= -238 ) {
      document.querySelector(main).style.marginLeft = '14rem';
      document.querySelector(footer).style.marginLeft = '14rem';
    } else {
      document.querySelector(main).style.marginLeft = 'auto';
      document.querySelector(footer).style.marginLeft = 'auto';
    }
  }

  function stickElement(selector, newClass, limit = 120) {
    // Get the current scroll value
    let BrowserHeight = document.documentElement.scrollTop || document.body.scrollTop;
    // If the scroll value is greater than the window height, let's add a class to the scroll-to-top button to show it!
    if (BrowserHeight > limit) {
      document.querySelector(selector).classList.add(newClass);
    } else {
      document.querySelector(selector).classList.remove(newClass);
    }
  }

document.querySelector('#header').addEventListener("click", (e) => {
  console.log(e.target);
})

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

  // back to top button
  document.querySelector(".back-to-top").addEventListener("click", (event) => {
    event.preventDefault();
    scrollToTop();
  });


  window.addEventListener("load", () => {
    stickElement(".back-to-top", "show-toTop-btn", 190)
    giveBodyMargin()
  });

  window.addEventListener("resize", () => {
    console.log(11);
    giveBodyMargin()
  })

  window.addEventListener("scroll", () => {
    stickElement(".back-to-top", "show-toTop-btn", 190)
  });

  // Initiate the wowjs animation library
  new WOW().init();

  document.querySelectorAll('.tooltip-demo')
    .forEach(tooltip => new bootstrap.Tooltip(tooltip, {
      selector: '[data-bs-toggle="tooltip"]'
    }))

  // add the class "active" to the clicked lick 
  document.querySelectorAll(".nav-item , .nav-link").forEach((element, i, parent) => {
    element.addEventListener("click", (e) => {
      for (element of parent) {
        element.classList.remove("active")
      }
      e.target.classList.add("active");
    })
  });

  document.querySelectorAll('[data-bs-toggle="popover"]')
    .forEach(popup => new bootstrap.Popover(popup))

  // Disable empty links
  $('a[href="#"], a[href=""]').attr('href', 'javascript:void(0)');

  // EventListener for toggle button to toggle btw dark and light mode 
  document.getElementById("dark-mode-toggle").addEventListener("click", (event) => {
    event.preventDefault();
    theme.changeIcon()
    setTimeout(function () {
      theme.toggleTheme(event)
    }, 300);
    console.log("Toggled!");
  });

  //Mobile nav

  // document.querySelector('.mobile-nav-toggle').addEventListener('click', (e) => {
  //   e.preventDefault()
  //   document.getElementById('mobile-nav').classList.toggle('mobile-nav-slide');
  // });



})(jQuery, Theme)
