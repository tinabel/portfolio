export const slideshow = () => {
  const slides = document.querySelectorAll("[data-slide]");
  const playButton = document.querySelector("[data-play]");
  const pauseButton = document.querySelector("[data-pause]");
  const prefersReducedMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  const hasSlides = slides.length > 0 && playButton && pauseButton;

  if (hasSlides) {
    slides[0].classList.add("active");
  }

  let currentSlide = 0;
  let intervalId;

  const showSlide = (slideIndex) => {
    slides.forEach((slide, index) => {
      if (index === currentSlide) {
        slide.classList.add("active");
      } else {
        slide.classList.remove("active");
      }
    });
    currentSlide = (slideIndex + slides.length) % slides.length;
  };

  const nextSlide = () => {
    currentSlide = (currentSlide + 1) % slides.length;
    showSlide(currentSlide);
  };

  const previousSlide = () => {
    currentSlide = (currentSlide - 1 + slides.length) % slides.length;
    showSlide(currentSlide);
  };

  const startSlideshow = () => {
    if (!hasSlides) {
      return;
    }

    intervalId = setInterval(nextSlide, 2500);
    playButton.classList.add("hidden");
    pauseButton.classList.remove("hidden");
  };

  const stopSlideshow = () => {
    clearInterval(intervalId);
    playButton.classList.remove("hidden");
    pauseButton.classList.add("hidden");
  };

  // Add event listeners for forward, backward, and stop buttons
 if (hasSlides) {
   playButton.addEventListener("click", () => {
     nextSlide();
     startSlideshow();
   });
   pauseButton.addEventListener("click", stopSlideshow);

   document.querySelector("[data-prev]").addEventListener("click", () => {
     clearInterval(intervalId);
     previousSlide();
     startSlideshow();
   });
   document.querySelector("[data-next]").addEventListener("click", () => {
     clearInterval(intervalId);
     nextSlide();
     startSlideshow();
   });

   if (!prefersReducedMotion) {
     startSlideshow();
   }
 }


};

export default {slideshow};
