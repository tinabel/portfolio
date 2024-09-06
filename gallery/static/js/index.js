import {ready} from "./utils.js";
import homepageSlideshow from "./homepageSlideshow.js";

ready(() => {
  document.body.classList.add('ready');
  homepageSlideshow.slideshow();
});
