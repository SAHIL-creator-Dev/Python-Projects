let currentFormId = null;
const toggleBtn = document.querySelector(".toggle_btn");
const toggleBtnIcon = document.querySelector(".toggle_btn i");
const dropdownMenu = document.querySelector(".dropdown_menu");
if (toggleBtn && toggleBtnIcon && dropdownMenu) {
  toggleBtn.onclick = function () {
    dropdownMenu.classList.toggle("open");
    const isOpen = dropdownMenu.classList.contains("open");
    toggleBtnIcon.classList = isOpen ? "fa-solid fa-xmark" : "fa-solid fa-bars";
  };
}

let slides = document.querySelectorAll(".home_page_slide");
let controls = document.querySelectorAll(".home_page_slider-controls span");
let progressBar = document.querySelector(".home_page_progress-bar");
let index = 0;

function showSlide(n) {
  slides.forEach((slide, i) => {
    slide.classList.toggle("active", i === n);
  });

  controls.forEach((dot, i) => {
    dot.classList.toggle("active", i === n);
  });

  progressBar.style.width = "0%";
  setTimeout(() => {
    progressBar.style.width = "100%";
  }, 100);
}

function nextSlide() {
  index = (index + 1) % slides.length;
  showSlide(index);
}

controls.forEach((dot, i) => {
  dot.addEventListener("click", () => {
    index = i;
    showSlide(index);
  });
});

setInterval(nextSlide, 5000); // Smoother 5s transition
showSlide(index);

// 
document.addEventListener("DOMContentLoaded", function () {
  const moreContainer = document.querySelector(".more_container_outer");

  if (!moreContainer) return;

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          requestAnimationFrame(() => {
            moreContainer.classList.add("visible");
            moreContainer.classList.remove("hidden");
          });
        } else {
          requestAnimationFrame(() => {
            moreContainer.classList.remove("visible");
            moreContainer.classList.add("hidden");
          });
        }
      });
    },
    { threshold: 0.3 }
  );

  observer.observe(moreContainer);
});


// 
document.addEventListener("DOMContentLoaded", function () {
  const eventContainer = document.querySelector(".event_section_body");

  if (!eventContainer) return;

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          requestAnimationFrame(() => {
            eventContainer.classList.add("visible");
            eventContainer.classList.remove("hidden");
          });
        } else {
          requestAnimationFrame(() => {
            eventContainer.classList.remove("visible");
            eventContainer.classList.add("hidden");
          });
        }
      });
    },
    { threshold: 0.3 }
  );

  observer.observe(eventContainer);
});


// 
document.addEventListener("DOMContentLoaded", function () {
  const aboutUsSection = document.querySelector(".about_us_home");

  if (!aboutUsSection) return;

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          requestAnimationFrame(() => {
            aboutUsSection.classList.add("visible");
            aboutUsSection.classList.remove("hidden");
          });
        } else {
          requestAnimationFrame(() => {
            aboutUsSection.classList.remove("visible");
            aboutUsSection.classList.add("hidden");
          });
        }
      });
    },
    { threshold: 0.3 }
  );

  observer.observe(aboutUsSection);
});



//delete detail script

function openModal(formId) {
  currentFormId = formId;
  document.getElementById("confirmationModal").style.display = "flex";
}

function closeModal() {
  currentFormId = null;
  document.getElementById("confirmationModal").style.display = "none";
}

function confirmDelete() {
  if (currentFormId) {
    document.getElementById(currentFormId).submit();
  }
  closeModal();
}
