const container = document.querySelector('[data-target="zoom"]');
const originalImage = document.querySelector('[data-target="zoom-image"]');
const largeImage = document.querySelector('[data-target="zoom-large-image"]');
const ZOOM_ACTIVE_CLASS = 'active';
const BORDER_STYLE = '1px solid #fff';
const OFFSET = '2rem';
const MAX_PERCENT = 95;
let isZoomed = false;

if (originalImage && largeImage) {
  largeImage.style.background = `url(${originalImage.src}) no-repeat #000`;
}

const zoomIn = (event) => {
  if (!isZoomed) {
    container.classList.remove(ZOOM_ACTIVE_CLASS);
    return;
  }

  container.classList.add(ZOOM_ACTIVE_CLASS);
  const el = event.target.getBoundingClientRect();
  const xRel = event.pageX - el.left;
  const yRel = event.pageY - el.top;
  const xPercent = Math.ceil((100 * xRel) / el.width);
  const yPercent = Math.ceil((100 * yRel) / el.height);

  largeImage.style.transform = `translate(-${xPercent}%, -${yPercent}%)`;
  largeImage.style.border = BORDER_STYLE;
  largeImage.style.display = 'block';
  largeImage.style.backgroundPosition = `${xPercent}% ${yPercent}%`;
  largeImage.style.left = xPercent <= MAX_PERCENT ? `calc(${xPercent}% + ${OFFSET})` : `calc(${xPercent}% - ${OFFSET})`;
  largeImage.style.top = yPercent <= MAX_PERCENT ? `calc(${yPercent}% + ${OFFSET})` : `calc(${yPercent}% - ${OFFSET})`;
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
};
