import {ready} from './utils.js';
import homepageSlideshow from './slideshow.js';

ready(() => {
  document.body.classList.add('ready');
  homepageSlideshow.slideshow();
});
