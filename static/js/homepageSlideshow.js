const slideshow = () => {
  console.log("BOOM");
  const slides = document.querySelectorAll("[data-slide]");
  let currentSlide = 0;
  let intervalId;

  const showSlide = (slideIndex) => {
    slides.forEach((slide, index) => {
      if (index === slideIndex) {
        slide.classList.replace("inactive", "active");
      } else {
        slide.classList.replace("active", "inactive");
      }
    });
  };

  const nextSlide = () => {
    currentSlide++;
    if (currentSlide >= slides.length) {
      currentSlide = 0;
    }
    showSlide(currentSlide);
  };

  const previousSlide = () => {
    currentSlide--;
    if (currentSlide < 0) {
      currentSlide = slides.length - 1;
    }
    showSlide(currentSlide);
  };

  const startSlideshow = () => {
    intervalId = setInterval(nextSlide, 2000);
  };

  const stopSlideshow = () => {
    clearInterval(intervalId);
  };

  slides.forEach((slide, index) => {
    slide.classList.replace("active", "inactive");
    if (index === 0) {
      slide.classList.replace("inactive", "active");
    }
  });

  // Add event listeners for forward, backward, and stop buttons
  // document.querySelector("[data-forward-button]").addEventListener("click", nextSlide);
  // document.querySelector("[data-backward-button]").addEventListener("click", previousSlide);
  // document.querySelector("[data-stop-button]").addEventListener("click", stopSlideshow);

  const prefersReducedMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  if (!prefersReducedMotion) {
    console.log("Starting slideshow...");
    startSlideshow();
  }
};