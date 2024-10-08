const container = document.querySelector('[data-target="zoom"]');
const originalImage = document.querySelector('[data-target*="zoom-image"]');
const largeImage = document.querySelector('[data-target="zoom-large-image"]');
const ZOOM_ACTIVE_CLASS = 'active';

let isZoomed = false;

if (originalImage && largeImage) {
  largeImage.style.background = `url(${originalImage.src}) no-repeat #000`;
}

const styleIt = (el, styles = {}) => {
  Object.keys(styles).forEach((key) => {
    el.style[key] = styles[key];
  });
};

const percentOf = (a, b) => {
  return Math.ceil((a * 100) / b);
};

const toRem = (value) => {
  return value / 16;
};

const zoomIn = (event) => {
  const el = event.target.getBoundingClientRect();
  const {
    width: imgWidth,
    height: imgHeight,
  } = el;

  let magnifierX = Number.parseInt(getComputedStyle(largeImage).width.split('px')[0]);
  let magnifierY = Number.parseInt(getComputedStyle(largeImage).height.split('px')[0]);

  const cursorX = event.pageX;
  const cursorY = event.pageY;
  const xRel = cursorX - el.left;
  const yRel = cursorY - el.top;
  const xPercent = percentOf(xRel, imgWidth);
  const yPercent = percentOf(yRel, imgHeight);

  let bubbleX = `${xRel}px`;
  let bubbleY = `${yRel}px`;

  largeImage.style.left = `${bubbleX}`;
  largeImage.style.top = `${bubbleY}`;

  let backgroundX = `${xPercent}%`;
  let backgroundY = `${yPercent}%`;

  if (yRel <= magnifierY / 4) {
    bubbleY = '0';
    backgroundY = `calc(${yPercent}% + 3rem)`;
  } else if (yRel >= (imgHeight - magnifierY)) {
    bubbleY = `${imgHeight - (magnifierY + 3)}px`;
    backgroundY = `calc(${yPercent}% - 3rem)`;
  } else {
    bubbleY = `${yRel}px`;
    backgroundY = `${yPercent}%`;
  }


  if (xRel <= magnifierX / 2) {
    // LEFT
    bubbleX = '0';
    backgroundX = `calc(${xPercent}% + 3rem - 3px)`;
  } else if (xRel <= imgWidth && xRel >= (imgWidth - (magnifierX))) {
    // RIGHT
    bubbleX = `${imgWidth - (magnifierX + 3)}px`;
    backgroundX = `calc(${xPercent}% - 3rem)`;
  } else {
    bubbleX = `${xRel}px`;
    backgroundX = `${xPercent}%`;
  }

  styleIt(largeImage, {
    display: 'block',
    backgroundPositionX: backgroundX,
    backgroundPositionY: backgroundY,
    left: bubbleX,
    top: bubbleY,
    transition: 'opacity 0.25s ease'
  });

  styleIt(originalImage, {
    PointerEvents: 'auto',
    userSelect: 'none'
  });

  container.classList.add(ZOOM_ACTIVE_CLASS);
};

const zoom = () => {
  isZoomed = !isZoomed;
  if (isZoomed) {
    container.classList.add(ZOOM_ACTIVE_CLASS);
    container.addEventListener('mousemove', zoomIn);
  } else {
    container.classList.remove(ZOOM_ACTIVE_CLASS);
    container.removeEventListener('mousemove', zoomIn);
  }
};

export const zoomInit = () => {
  if (!container) {
    return;
  }

  if (!isZoomed) {
    originalImage.addEventListener('click', zoom);

  } else {
    originalImage.removeEventListener('click', zoom);
  }
};
