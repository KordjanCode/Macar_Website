# coding: utf-8
import re

html = """
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    section {
      display: grid;
      place-items: center;
      align-content: center;
      min-height: 100vh;
    }

    .schedule-title {
      font-size: 24px;
      margin-bottom: 10px;
    }

    .schedule-table {
      border-collapse: collapse;
      text-align: center;
      width: 100%;
    }

    .schedule-table thead th {
      background-color: #f2f2f2;
      padding: 10px;
      font-weight: bold;
    }

    .schedule-table tbody td {
      padding: 10px;
      border-bottom: 1px solid #f2f2f2;
    }

    @media(max-width: 480px) {
      .schedule-table {
        font-size: 0.8rem;
      }
    }

    @import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&display=swap');

* {
  padding: 0;
  margin: 0;
  font-family: "Montserrat", sans-serif;
}

html {
  scroll-behavior: smooth;
}

body {
  margin-top: 70px;
  position: relative;
  height: 600vh;
  /* background: linear-gradient(to bottom, #e0e0e0 0%,#d3d3d3 93%, #000000 100%); */

}

header {
  transition: 0.6s ease-in-out;
  background-color: #060606;
  position: fixed;
  top: 0;
  width: 100%;
  z-index: 2;
}

h1 {
  font-size: 36px;
  text-align: center;
  padding: 5vh;

}

h2 {
  font-size: 20px;
  padding: 8vw;
  text-align: center;
}

h3 {
  font-size: 20px;
  padding: 1vh;
  margin-left: 15vw;
  margin-right: 15vw;
  text-align: center;
}

h4 {
  padding: 1vw;

}

a {
  color: #acacac;
  text-decoration: none;
}

.container {
  width: 1600px;
  margin: auto;
}

.subcontainer {
  width: 100%;
  margin: auto;
}

/* ------------------------------------------NAVBAR----------------------------------- */
.navbar-container {
  min-height: 70px;
  display: flex;
  justify-content: space-around;
}

.navbar-left {
  margin-left: 5vw;
  display: flex;
  justify-content: space-around;
  align-items: center;
  gap: 50px;
}

.navbar-left span {
  color: #ff0000;
  font-weight: bold;
}

.nav-branding-1,
.nav-branding-2 {
  color: white;
  font-size: 2rem;
}

.nav-branding-2 {
  opacity: 0;
  display: none;
  padding: 15px 0;
  width: 100%;
  border-bottom: 1px solid rgba(211, 211, 211, 0.2);
}

.nav-menu {
  display: flex;
  justify-content: flex-start;
  justify-content: space-around;
  align-items: center;
  gap: 40px;
}

.nav-link {
  width: 100%;
  transition: 0.3s;
  padding: 20px 0;
}

.nav-link:hover {
  color: #059DFF;
}

.login-link {
  display: none;
}

.hamburger {
  display: none;
  cursor: pointer;
}

.bar {
  display: block;
  width: 25px;
  height: 3px;
  margin: 5px auto;
  -webkit-transition: all 0.3s ease;
  transition: all 0.3s ease;
  background-color: white;
}

/* -------------------------------------------------RIGHT NAV BAR--------------------------------------------------------- */

.navbar-right {
  margin-right: 5vw;
  width: 100%;
  display: flex;
  justify-content: flex-end;
  align-items: center;
  gap: 10px;
}

/* .navbar-right button {
  padding: 10px;
  border-radius: 5px;
  width: 70px;
  color: white;
  border: none;
  font-weight: bold;
  font-family: inherit;
  display: block;
  background-image: linear-gradient(180deg, #f1f1f1, #ff0000);
} */

.lang-btn {
  background-color: transparent;
  color: white;
  font-weight: bold;
  font-family: inherit;
  font-size: 0.8rem;
  padding: 10px;
  border: 1px solid white;
  border-radius: 5px;
  cursor: pointer;
  transition: 0.3s;
}

.lang-btn:hover {
  background-color: rgb(222, 13, 13);
}


/* -------------------------------------------------SECTIONS--------------------------------------------------------------- */

.section-container {

  display: block;
}


#home {
  background-color: white;

}

#about {
  background-color: white;


}

/* ----------------------------------------------------PHOTO--------------------------- */
#photos {
  background-color: white;
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin-top: 15vh;

}

.photos-container {
  overflow-x: hidden;
  max-height: 75vh;

}

.swiper {
  width: 80vw;
  height: 60vh;
  margin-left: auto;
  margin-right: auto;

}

.swiper-slide {
  text-align: center;
  font-size: 18px;
  background: #fff;
  display: flex;
  justify-content: center;
  align-items: center;
}

.swiper-slide img {
  display: block;
  width: 100%;
  height: 100%;
  max-height: 75vh;
  min-height: 75vh;
  object-fit: cover;
}


#location {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

#contact {
  background-color: white;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.home-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  align-self: center;
}

.home-image-container img {
  max-width: 20vh;
  max-height: 20vh;

}

.about-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;

}

.about-description-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.about-certificates-container {
  display: flex;
  justify-content: space-around;
  align-items: center;

  max-height: 30vh;

}

.about-certificates-container img {
  margin: 5vw;
  height: 15vw;
  max-width: 100%;
  max-height: 100%;
}

.about-certificates-container:nth-child(2) {
  height: 20vw;
}

.google-map {
  margin-bottom: 5vh;
  width: 70vw;
  height: 50vh;
  border-radius: 20px;
  border: 1px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  max-width: 1000px;



}

/* ----------------------------------------------------Animations--------------------------- */

#NoTranslateX {
  transform: none;
}

.hidden {
  opacity: 0;
  filter: blur(5px);
  ;
  transform: scale(115%);
  transition: All 0.7s;
}

.show {
  opacity: 1;
  filter: blur(0);
  transform: scale(100%);
}

.lang-btn-delay {
  transition-delay: 600ms;
}

.logo:nth-child(2) {
  transition-delay: 100ms;
}

.logo:nth-child(3) {
  transition-delay: 200ms;
}

.logo:nth-child(4) {
  transition-delay: 300ms;
}

.logo:nth-child(5) {
  transition-delay: 400ms;
}


/* ----------------------------------------------------CONTACT CARD ------------------------------ */
.contact-card {
  width: 300px;
  background-color: white;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  margin: 20px;
  display: inline-block;
}

.contact-info {
  padding: 20px;
  text-align: center;
}

.contact-info img {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  object-fit: cover;
  margin-bottom: 10px;
}

.contact-info h2 {
  margin: 0;
}

.contact-info p {
  margin: 5px 0;
}

.contact-info a {
  color: black;
  text-decoration: none;
  transition: color 0.3s ease;
}

.contact-info a:hover {
  color: blue;
}


/* -------------------------------------------------900px------------------------------------------------------------------ */


@media(max-width:1600px) {
  .container {
    width: 100%;
  }
}

@media(max-width:820px) {

  h1 {
    font-size: 5vw;
    margin-left: 5vw;
    margin-right: 5vw;
  }

  h2 {
    font-size: 3vw;
    margin-left: 5vw;
    margin-right: 5vw;
  }

  h3 {
    font-size: 4vw;
    margin-left: 5vw;
    margin-right: 5vw;
  }

  .hamburger {
    display: block;
  }

  .hamburger.active .bar:nth-child(2) {
    opacity: 0;
  }

  .hamburger.active .bar:nth-child(1) {
    transform: translateY(8px) rotate(45deg);
  }

  .hamburger.active .bar:nth-child(3) {
    transform: translateY(-8px) rotate(-45deg);
  }

  .nav-menu {
    position: fixed;
    width: 300px;
    left: -340px;
    top: 0;
    min-height: 100vh;
    padding: 0 20px;
    flex-direction: column;
    gap: 0;
    transition: 0.3s;
    background-color: #060606;
  }

  .nav-branding-2.active {
    opacity: 1;
    display: block;
  }

  .nav-link {
    padding: 15px 0;
  }

  .login-link {
    display: block;
  }

  .navbar-right button {
    display: none;
  }

  .nav-menu.active {
    left: 0;
  }

  .showcase-header {
    width: 100%;
    margin: auto;
  }

}

@media(max-width:480px) {
  .nav-menu {
    width: 200px;
    left: -240px;
  }
}
  </style>

  <title>Macar_Website</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@10/swiper-bundle.min.css" />
  <script src="https://cdn.jsdelivr.net/npm/swiper@10/swiper-bundle.min.js"></script>
  <link rel="stylesheet" href="style.css">


  <script src="/swiper-bundle.min.css"></script>

  <script defer src="/app.js"></script>


</head>
<header id="header">
  <div class="container">
    <div class="subcontainer">

      <nav class="navbar-container">

        <div class="navbar-left">
          <a href="#" class="nav-branding-1 logo hidden">MA<span>CAR</span></a>
          <div class="nav-menu">
            <a href="#" class="nav-branding-2 logo hidden">MA<span>CAR</span></a>

            <a href="#about" class="nav-link logo hidden">Normy</a>
            <a href="#photos" class="nav-link logo hidden">Realizacje</a>
            <a href="#location" class="nav-link logo hidden">Lokalizacja</a>
            <a href="#contact" class="nav-link logo hidden">Kontakt</a>
            <a href="#" class="nav-link login-link">Login</a>
          </div>
        </div>

        <div class="navbar-right">
          <button id="language-switch" class="lang-btn lang-btn-delay hidden">English</button>
          <div class="hamburger">
            <span class="bar"></span>
            <span class="bar"></span>
            <span class="bar"></span>
          </div>
        </div>
      </nav>
    </div>
  </div>
</header>

<body>

  <section id="home">
    <div class="home-container">

      <h1 class="hidden logo">Tarcza Ochronna Twojego Biznesu!</h1>
      <h2 class="hidden logo">Błyskawiczny montaz tryskaczy przeciwpozarowych dla bezpieczenstwa, na którym możesz
        polegac.</h2>
      <div class="hidden logo home-image-container">
        <img src="./img/logo_fire_shield.png" alt="FireShield 1">
      </div>
    </div>

  </section>

  <section id="about">
    <div class="about-container">
      <div class="about-headline-container logo hidden">
        <h1>Macar<br>
          Twoja Tarcza Ochronna!</h1>
      </div>
      <div class="about-description-container">
        <h3 class="logo hidden">Specjaliści od niezawodnych tryskaczy przeciwpożarowych, które chronią Twój biznes.
        </h3>
        <h3 class="logo hidden">Nasze systemy posiadają najwyższe normy przeciwpożarowe zarówno Polskie, ustalane przez
          Polski Komitet
          Normalizacyjny (PKN), jak i Europejskie (VDS) oraz międzynarodowe (NFPA) gwarantując najwyższe standardy
          bezpieczeństwa.</h3>
        <h3 class="logo hidden">Wybierając Macar, inwestujesz w szybkość, rzetelność i profesjonalizm. Skontaktuj się z
          nami i zadbaj o
          bezpieczeństwo swojej firmy już dziś!</h3>
      </div>
      <div class="about-certificates-container">
        <img src="./img/logo_vds.png" alt="Logo 1" class="logo hidden">
        <img src="./img/logo_pkn.jpeg" alt="Logo 2" class="logo hidden">
        <img src="./img/logo_NFPA.png" alt="Logo 3" class="logo hidden">
      </div>
    </div>
  </section>

  <section id="photos" class="hidden">

    <div class="photo-section-headline">
      <h1>Realizacje</h1>
    </div>
    <div class="photos-container">
      <div class="swiper mySwiper">
        <div class="swiper-wrapper">
          <div class="swiper-slide"><img src="./img/photos/photo_1.jpeg" alt="Photo 1"></div>
          <div class="swiper-slide"><img src="./img/photos/photo_2.jpeg" alt="Photo 2"></div>
          <div class="swiper-slide"><img src="./img/photos/photo_3.jpeg" alt="Photo 3"></div>
          <div class="swiper-slide"><img src="./img/photos/photo_4.jpeg" alt="Photo 4"></div>
        </div>
        <div class="swiper-button-next"></div>
        <div class="swiper-button-prev"></div>
        <div class="swiper-pagination"></div>
      </div>
    </div>

  </section>

  <section id="location">
    <h1 class="hidden logo">Znajdź Nas!</h1>

    <iframe class="google-map hidden logo"
      src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2362.5144178124174!2d17.52294131580203!3d53.691279256519316!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x470247c9a2924e33%3A0x53d8ccd45442f033!2sTopole%2011%2C%2089-600%20Chojnice!5e0!3m2!1sen!2spl!4v1678659172594!5m2!1sen!2spl"
      style="display:flex;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade">
    </iframe>
    <h3 class="map-text">Zlokalizowani na pomorzu, realizujemy zlecenia w całej Polsce oraz Europie</h3>
    </div>
  </section>

  <section id="contact">
    <h1 class="logo hidden">Jak możemy pomóc?</h1>
    <div class="contact-card logo hidden">
      <div class="contact-info">
        <img src="./img/photos/photo_1.jpeg" alt="Profile Photo">
        <h4>Piotr</h4>
        <p>Właściciel</p>
        <p>Telefon: <a href="tel:+48 794 724 857">+48 794 724 857</a></p>
        <p>Email: <a href="mailto:biuromacar@gmail.com">biuromacar@gmail.com</a></p>
      </div>
    </div>
  </section>
  <section id="schedule">

    <h1 class="schedule-title logo hidden">Zapraszamy</h1>
    <table class="schedule-table logo hidden">
      <thead>
        <tr>
          <th>Dzień Tygodnia</th>
          <th>Godzina Otwarcia</th>
          <th>Godzina Zamknięcia</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Poniedziałek</td>
          <td>8:00</td>
          <td>18:00</td>
        </tr>
        <tr>
          <td>Wtorek</td>
          <td>8:00</td>
          <td>18:00</td>
        </tr>
        <tr>
          <td>Środa</td>
          <td>8:00</td>
          <td>18:00</td>
        </tr>
        <tr>
          <td>Czwartek</td>
          <td>8:00</td>
          <td>18:00</td>
        </tr>
        <tr>
          <td>Piątek</td>
          <td>8:00</td>
          <td>18:00</td>
        </tr>
        <tr>
          <td>Sobota</td>
          <td>8:00</td>
          <td>15:00</td>
        </tr>
        <tr>
          <td>Niedziela</td>
          <td>Zamknięte</td>
          <td>Zamknięte</td>
        </tr>
      </tbody>
    </table>

  </section>
</body>
<script src="script.js"></script>

</html>

"""

# Extract all CSS classes from the HTML
classes = re.findall(r'class="(.*?)"', html)

# Create a set of unique classes
all_classes = set(classes)

# Find the used classes in the HTML
used_classes = set(re.findall(r'(?<=class=")(.*?)(?=")', html))

# Find the unused classes
unused_classes = all_classes - used_classes

# Print the unused classes
print("Unused classes:")
for class_name in unused_classes:
    print(class_name)
