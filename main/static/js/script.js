document.addEventListener("DOMContentLoaded", (event) => {
	const menuToggle = document.getElementById("menu-toggle");
	const menu = document.getElementById("menu");

	menuToggle.addEventListener("click", () => {
		menu.classList.toggle("active");
		menuToggle.classList.toggle("active");
	});

	// Close menu when clicking outside
	document.addEventListener("click", (event) => {
		if (
			!menu.contains(event.target) &&
			!menuToggle.contains(event.target)
		) {
			menu.classList.remove("active");
			menuToggle.classList.remove("active");
		}
	});

	// Smooth scrolling for anchor links
	document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
		anchor.addEventListener("click", function (e) {
			e.preventDefault();

			document.querySelector(this.getAttribute("href")).scrollIntoView({
				behavior: "smooth",
			});

			// Close menu after clicking a link (for mobile)
			menu.classList.remove("active");
			menuToggle.classList.remove("active");
		});
	});

	// Add active class to nav links when scrolling
	const sections = document.querySelectorAll("section");
	const navLinks = document.querySelectorAll(".nav-link");

	window.addEventListener("scroll", () => {
		let current = "";
		sections.forEach((section) => {
			const sectionTop = section.offsetTop;
			const sectionHeight = section.clientHeight;
			if (pageYOffset >= sectionTop - sectionHeight / 3) {
				current = section.getAttribute("id");
			}
		});

		navLinks.forEach((link) => {
			link.classList.remove("active");
			if (link.getAttribute("href").slice(1) === current) {
				link.classList.add("active");
			}
		});
	});
});

// experience
document.addEventListener("DOMContentLoaded", () => {
	const tabButtons = document.querySelectorAll(".tab-button");
	const tabContents = document.querySelectorAll(".tab-content");

	tabButtons.forEach((button, index) => {
		button.addEventListener("click", () => {
			tabButtons.forEach((btn) => btn.classList.remove("active"));
			tabContents.forEach((content) =>
				content.classList.remove("active")
			);

			button.classList.add("active");
			document.getElementById(`tab-${index}`).classList.add("active");
		});
	});
});

document.addEventListener("DOMContentLoaded", () => {
	document.querySelectorAll(".image-viewer").forEach((viewer) => {
		const images = viewer.querySelectorAll(".viewer-img");
		const dots = viewer.querySelectorAll(".dot");

		dots.forEach((dot, i) => {
			dot.addEventListener("click", () => {
				// Hide all images and deactivate all dots
				images.forEach((img) => img.classList.add("hidden"));
				dots.forEach((d) => d.classList.remove("active"));

				// Show selected image and activate corresponding dot
				images[i].classList.remove("hidden");
				dot.classList.add("active");
			});
		});
	});
});
