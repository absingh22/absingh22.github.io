// Home Section
document.addEventListener("DOMContentLoaded", () => {
	const typedElement = document.querySelector(".typed");
	const items = typedElement.getAttribute("data-typed-items").split(", ");
	let currentIndex = 0;
	let charIndex = 0;
	let typing = true;

	function typeEffect() {
		const currentText = items[currentIndex];

		if (typing) {
			charIndex++;
			if (charIndex === currentText.length + 1) {
				typing = false;
				setTimeout(typeEffect, 1000); // Pause before deleting
				return;
			}
		} else {
			charIndex--;
			if (charIndex === 0) {
				typing = true;
				currentIndex = (currentIndex + 1) % items.length; // Move to next word
			}
		}

		typedElement.textContent = currentText.slice(0, charIndex);
		setTimeout(typeEffect, typing ? 100 : 50); // Typing and deleting speeds
	}

	typeEffect();
});

// About Section
// Projects Section
document.addEventListener("DOMContentLoaded", function () {
	const tags = document.querySelectorAll(".tag");
	const projects = document.querySelectorAll(".project-item");
	// Tag-based filtering
	tags.forEach((tag) => {
		tag.addEventListener("click", function () {
			const selectedTag = this.getAttribute("data-tag");

			if (selectedTag === "all") {
				// Show all projects
				projects.forEach((project) => {
					project.style.display = "";
				});
			} else {
				// Filter projects by tag
				projects.forEach((project) => {
					const projectTags = project.getAttribute("data-tag");
					if (projectTags.includes(selectedTag)) {
						project.style.display = "";
					} else {
						project.style.display = "none";
					}
				});
			}

			// Optional: Highlight the selected tag
			tags.forEach((tag) => tag.classList.remove("active"));
			this.classList.add("active");
		});
	});
});

// Experiences Section
// Skills Section
// Contact Section
