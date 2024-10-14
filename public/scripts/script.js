// --------------------------- HAMBURGER MENU ------------------------

const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav-menu");
const navBranding = document.querySelector(".nav-branding-2");

hamburger.addEventListener("click", () => {
  hamburger.classList.toggle("active");
  navMenu.classList.toggle("active");
  navBranding.classList.toggle("active");
})

document.querySelectorAll(".nav-link").forEach(n => n.addEventListener("click", () => {
  hamburger.classList.remove("active");
  navMenu.classList.remove("active");
}))

// ----------------------------------------- LANGUAGE SWITCH ------------------------------

let languageSwitch = document.querySelector('#language-switch');
let pageTitle = document.querySelector('title');
let homeTitle = document.querySelector('#home h1');
let homeTitleDescription = document.querySelector('#home h2');
let aboutTitle = document.querySelector('#about h1');
let photosTitle = document.querySelector('#photos h1');
let locationTitle = document.querySelector('#location h1');
let contactTitle = document.querySelector('#contact h1');
let scheduleTitle = document.querySelector('#schedule h1');

let switchLanguage = function () {
  if (languageSwitch.innerHTML === 'English') { //if language is currently Polish
    languageSwitch.innerHTML = 'Polski';
    pageTitle.innerHTML = 'Macar_Website';
    homeTitle.innerHTML = 'Fire protection systems for Your Buisness';
    homeTitleDescription.innerHTML = 'Express Montage of Fire Protection Services, which you can rely on!'
    aboutTitle.innerHTML = 'Certificates, confirmation of the quality of services provided';
    photosTitle.innerHTML = 'Photos';
    locationTitle.innerHTML = 'Location';
    contactTitle.innerHTMLą = 'Contact';
    scheduleTitle.innerHTML = 'Working Hours';
  } else { //if language is currently English
    languageSwitch.innerHTML = 'English';
    pageTitle.innerHTML = 'Strona internetowa Macar';
    homeTitle.innerHTML = 'Tarcza Ochronna Twojego Biznesu!';
    homeTitleDescription.innerHTML = 'Błyskawiczny montaż tryskaczy przeciwpożarowych dla bezpieczeństwa, na którym możesz polegać.'
    aboutTitle.innerHTML = 'Atesty, potwierdzenie jakości wykonywanych usług';
    photosTitle.innerHTML = 'Galeria zdjęć';
    locationTitle.innerHTML = 'Lokalizacja';
    contactTitle.innerHTML = 'Kontakt';
    scheduleTitle.innerHTML = 'Godziny pracy';
  }
};

languageSwitch.addEventListener('click', switchLanguage);


// ----------------------------------------- PHOTO SWIPER ----------------------------------------------


var swiper = new Swiper(".mySwiper", {
  slidesPerView: 1,
  spaceBetween: 30,
  loop: true,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  freeMode:{
    enabled: true,
    sticky: true,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
});