import {ready} from './utils.js';
import homepageSlideshow from './slideshow.js';
import {navigation} from './navigation.js';
import {modalInit} from './modal.js';
import {zoomInit} from './zoom.js';

ready(() => {
  modalInit();
  navigation();
  zoomInit();
  document.body.classList.add('loaded');
  homepageSlideshow.slideshow();
});
