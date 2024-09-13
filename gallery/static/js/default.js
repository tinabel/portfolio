import {ready} from './utils.js';
import homepageSlideshow from './slideshow.js';
import {navigation} from './navigation.js';
import {modalInit} from './modal.js';

ready(() => {
  modalInit();
  navigation();
  document.body.classList.add('loaded');
  homepageSlideshow.slideshow();
});
