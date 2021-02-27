// a dark Mode API
export const Theme = ( function () {  
	const prefersDarkScheme = window.matchMedia("(prefers-color-scheme: dark)");

	// onload function to load the correct theme from the localStorage
	window.addEventListener("DOMContentLoaded", () => {
		const currentTheme = localStorage.getItem("theme");
		if (currentTheme == "dark") {
			setTimeout(function () {
				document.body.classList.toggle("dark-theme");
			}, 500);
			changeIcon()
		} else if (currentTheme == "light") {
			document.body.classList.toggle("light-theme");
		}
	});

	function changeIcon() {
		document.getElementById("switch-theme").classList.toggle("active");
	}
	
	return {
		//toggling our day and night icons
		changeIcon:changeIcon,

		 toggleTheme: function (event) {
		 	event.preventDefault()
		 	let theme
		 	// check if dark mode is enabled
		 	if (prefersDarkScheme.matches) {
		 		document.body.classList.toggle("light-theme");
		 		theme = document.body.classList.contains("light-theme") ?
		 			"light" :
		 			"dark";
		 	} else {
		 		document.body.classList.toggle("dark-theme");
		 		theme = document.body.classList.contains("dark-theme") ? "dark" : "light";
		 	}
		 	// update the current theme and storing it to the localStorage
		 	localStorage.setItem('theme', theme)
		 	console.log(theme);
		 },


	}
})();
