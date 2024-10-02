export const ready = (fn) => {
  if (document.readyState !== 'loading') {
    fn();
  } else {
    document.addEventListener('DOMContentLoaded', fn);
  }
};

const imageObserver = new IntersectionObserver(function(entries, observer) {
  entries.forEach(function(entry) {
    if (entry.isIntersecting) {
      var image = entry.target;
      image.src = image.dataset.src;
      imageObserver.unobserve(image);
    }
  });
});


export const loader = () => {
  let lazyImages;
  if ("IntersectionObserver" in window) {
    lazyImages = document.querySelectorAll('img[data-target="lazy-image"]');
    var imageObserver = new IntersectionObserver(function(entries, observer) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          var image = entry.target;
          image.src = image.dataset.src;
          image.classList.remove("lazy");
          imageObserver.unobserve(image);
        }
      });
    });

    lazyImages.forEach(function(image) {
      imageObserver.observe(image);
    });
  } else {
    let loadThrottleTimeout;
    lazyImages = document.querySelectorAll('img[data-target="lazy-image"]');

    function lazyload() {
      if (loadThrottleTimeout) {
        clearTimeout(loadThrottleTimeout);
      }

      loadThrottleTimeout = setTimeout(function() {
        let scrollTop = window.scrollY;
        lazyImages.forEach(function(img) {
          if (img.offsetTop < (window.innerHeight + scrollTop)) {
            img.src = img.dataset.src;
          }
        });
        if (lazyImages.length == 0) {
          document.removeEventListener("scroll", lazyload);
          window.removeEventListener("resize", lazyload);
          window.removeEventListener("orientationChange", lazyload);
        }
      }, 20);
    }

    document.addEventListener("scroll", lazyload);
    window.addEventListener("resize", lazyload);
    window.addEventListener("orientationChange", lazyload);
  }
};


