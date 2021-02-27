// Our TypeWriter Class
class TypeWriter {
  constructor(txtElement, words, wait = 3000) {
    this.txtElement = txtElement;
    this.words = words;
    this.txt = "";
    this.wordIndex = 0;
    this.wait = parseInt(wait, 10);
    this.type();
    this.isDeleting = false;
  }
  //Type Method
  type() {
    // Getting the current index of word
    const current = this.wordIndex % this.words.length;
    // Getting the full text of the word at the current index
    const fullText = this.words[current];

    // the variable that will determine our typing speed
    let typeSpeed = 300;
    //Checking to see if we deleting or typing text
    if (this.isDeleting) {
      typeSpeed /= 2;
      //Remove Letters in words
      this.txt = fullText.substr(0, this.txt.length - 1);
    } else {
      //Adding Letters in words
      this.txt = fullText.substr(0, this.txt.length + 1);
    }
    // inserting text into DOM
    this.txtElement.innerHTML = `<span class="txt">${this.txt}</span>`;

    // checking to see if we are done typing
    if (!this.isDeleting && this.txt === fullText) {
      //Make a pause at end
      typeSpeed = this.wait;
      // Set delete to True
      this.isDeleting = true;
    } else if (this.isDeleting && this.txt === "") {
      this.isDeleting = false;
      //Move to next word
      this.wordIndex++;
      //pause before typing
      typeSpeed = 700;
    }
    setTimeout(() => {
      this.type();
    }, typeSpeed);
  }
}

function init() {
  const txtElement = document.querySelector(".txt-type");
  const words = JSON.parse(txtElement.getAttribute("data-words"));
  const wait = txtElement.getAttribute("data-wait");
  //initialize the TypeWriter
  new TypeWriter(txtElement, words, wait);
}

// Init On DOM Load
document.addEventListener("DOMContentLoaded", init);

console.trace("This Page Has Loaded");
