const container = document.querySelector('[data-target="zoom"]');
const originalImage = document.querySelector('[data-target="zoom-image"]');
const largeImage = document.querySelector('[data-target="zoom-large-image"]');
const ZOOM_ACTIVE_CLASS = 'active';
const OFFSET = 2;
const MAX_PERCENT = 95;
let isZoomed = false;

if (originalImage && largeImage) {
  largeImage.style.background = `url(${originalImage.src}) no-repeat #000`;
}

const percentOf = (a, b) => {
  return Math.ceil((a * 100) / b);
};

const toRem = (value) => {
  return value / 16;
};

const zoomIn = (event) => {
  if (!isZoomed) {
    container.classList.remove(ZOOM_ACTIVE_CLASS);
    return;
  }

  const el = event.target.getBoundingClientRect();

  const originalWidth = originalImage.naturalWidth;
  const originalHeight = originalImage.naturalHeight;

  const {
    width: imgWidth,
    height: imgHeight,
    left: imgLeft,
    top: imgTop,
    bottom: imgBottom,
    right: imgRight
  } = el;

  const imgPercentWidth = percentOf(imgWidth, originalWidth);
  const imgPercentHeight = percentOf(imgHeight, originalHeight);

  let magnifierX = Number.parseInt(getComputedStyle(largeImage).width.split('px')[0]);
  let magnifierY = Number.parseInt(getComputedStyle(largeImage).height.split('px')[0]);

  const cursorX = event.pageX;
  const cursorY = event.pageY;
  const xRel = cursorX - (el.left);
  const yRel = cursorY - (el.top);
  const xPercent = percentOf(xRel, imgWidth);
  const yPercent = percentOf(yRel, imgHeight);

  let bubbleX = `${xRel}px`;
  let bubbleY = `${yRel}px`;

  largeImage.style.left = `${bubbleX}`;
  largeImage.style.top = `${bubbleY}`;

  let backgroundX = `${xPercent}%`;
  let backgroundY = `${yPercent}%`;

  console.log(xRel, yRel, xPercent, yPercent);
  if (yRel <= imgTop + magnifierY) {
    bubbleY = '1rem';
    backgroundY = `calc(${yPercent}% - ${toRem(magnifierY) * 1.5}rem)`;
    // backgroundY = `calc(${yPercent}% - ${toRem(magnifierY) + ((imgPercentHeight / 100) * (OFFSET * 2))}rem)`;
  } else if (yRel >= (imgHeight - ((magnifierY / 2) + 64))) {
    console.log("BOTTOM EDGE HIT");
    // bubbleY = `${yRel - (magnifierY + 32);} px`;
    backgroundY = `calc(${yPercent}% - ${toRem(magnifierY)}rem)`;
  } else {
    bubbleY = `${yRel - (OFFSET * 2)} px`;
    backgroundY = `calc(${yPercent}% )`;
  }


  if (xRel <= ((imgLeft - 1) + (magnifierX / 2))) {
    // LEFT
    console.log("LEFT EDGE HIT");
    bubbleX = '1rem';
    backgroundX = `calc(${xPercent}% - 1rem)`;
    // backgroundX = `calc(${xPercent}% + ${(imgPercentWidth / 100) * (OFFSET * 2)}rem)`;
  } else if (xRel >= (imgWidth - (magnifierX + 16))) {
    // RIGHT
    console.log("RIGHT EDGE HIT");
    // bubbleX = `${xRel - (magnifierX + 32);} px`;
    backgroundX = `calc(${xPercent}% + ${magnifierX + 64}px)`;
  } else {
    // bubbleX = `${xRel;} px`;
    backgroundX = `calc(${xPercent}% + ${magnifierX - (OFFSET * 16)}px)`;
  }


  largeImage.style.display = 'block';
  largeImage.style.backgroundPositionX = backgroundX;
  largeImage.style.backgroundPositionY = backgroundY;
  largeImage.style.left = `${bubbleX}`;
  largeImage.style.top = `${bubbleY}`;
  // largeImage.style.transform = `translate(${bubbleX}, ${bubbleY})`;
  largeImage.style.transition = 'opacity 1s ease, left 0.25s ease';
  container.classList.add(ZOOM_ACTIVE_CLASS);
};

const zoom = () => {
  isZoomed = !isZoomed;
  container.classList.toggle(ZOOM_ACTIVE_CLASS);
  if (isZoomed) {
    container.addEventListener('mousemove', zoomIn);
  } else {
    container.removeEventListener('mousemove', zoomIn);
  }
};

export const zoomInit = () => {
  if (!container) {
    console.error('Zoom container not found');
    return;
  }
  container.addEventListener('click', zoom);
};;;
