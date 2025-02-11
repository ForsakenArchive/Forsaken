from flask import Flask, render_template_string, send_from_directory
import os

app = Flask(__name__)

# Add route to serve static files
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory(os.getcwd(), filename)

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta name="title" content="The Forsaken">
    <meta name="description" content="An archive for the interconnected stories by Forsaken.">
    <meta name="keywords" content="Forsaken Verse, TheForsaken, The Forsaken, Forsaken, Forsaken Archive, Archive, eerie, Novel, Novels, books, book, Survival, Loss, Family, Struggle, Desperation, Hope, Tragedy, Betrayal, supernatural, sci-fi, bright fantasy, dark fantasy, epic, mysteries, suspense, adventure, psychological thriller, dystopian, supernatural creatures, forbidden knowledge, power, redemption, destiny, twists, betrayals, fate, conspiracy, mysteries, secrets, haunted, legends, ancient, revenge, harem, ecchi, illusions, dangerous world, history, family bonds, battle, broken, war, desitny, jjk, jujutsu kaisen, anime, manga, manhwa, manhua">
    <meta name="theme-color" content="#7B68EE">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://theforsaken.netlify.app/">
    <meta property="og:site_name" content="The Foresaken">
    <meta property="og:title" content="The Foresaken Verse">
    <meta property="og:description" content="An archive for the interconnected stories by Forsaken.">
    <meta property="og:image" itemprop="image" content="">
    <meta property="og:image:secure_url" itemprop="image" content="">
    <meta property="og:image:type" content="image/png">
    <meta property="og:image:width" content="200">
    <meta property="og:image:height" content="200">
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Forsaken</title>
  <!-- FONTS -->
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
  <style>
    /* BASE STYLES */
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }
    html {
      scroll-behavior: smooth;
    }
    body {
      font-family: 'Roboto', sans-serif;
      background: #121212;
      color: #e0e0e0;
      line-height: 1.6;
      overflow-x: hidden;
    }
    a {
      text-decoration: none;
      color: inherit;
    }

    /* HEADER / NAV */
    header {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      padding: 20px 50px;
      background: rgba(18, 18, 18, 0.9);
      backdrop-filter: blur(10px);
      z-index: 1000;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    header .brand {
      font-family: 'Cinzel', serif;
      font-size: 1.8rem;
      color: #fff;
    }
    /* Nav links */
    nav ul {
      display: flex;
      list-style: none;
    }
    nav ul li {
      margin-left: 30px;
    }
    nav ul li a {
      font-size: 1rem;
      font-weight: 500;
      transition: color 0.3s;
    }
    nav ul li a:hover {
      color: #7B68EE;
    }
    /* Ham */
    .menu-toggle {
      display: none;
      flex-direction: column;
      cursor: pointer;
    }
    .menu-toggle .bar {
      width: 25px;
      height: 3px;
      background-color: #fff;
      margin: 4px 0;
      transition: 0.3s;
    }

    /* HERO SECTION */
    .hero {
      position: relative;
      height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      text-align: center;
      padding: 0 20px;
      background: linear-gradient(135deg, #7B68EE 0%, #1e1e1e 100%);
    }
    .hero .hero-content {
      max-width: 800px;
    }
    .hero h1 {
      font-family: 'Cinzel', serif;
      font-size: 3rem;
      margin-bottom: 20px;
    }
    .hero p {
      font-size: 1.2rem;
      margin-bottom: 40px;
      line-height: 1.4;
    }
    .hero a.btn {
      padding: 12px 30px;
      border: 2px solid #7B68EE;
      color: #7B68EE;
      font-weight: 500;
      transition: background 0.3s, color 0.3s;
    }
    .hero a.btn:hover {
      background: #7B68EE;
      color: #fff;
    }

    /* SECTIONS */
    section {
      padding: 100px 20px;
    }
    .section-title {
      text-align: center;
      font-family: 'Cinzel', serif;
      font-size: 2.5rem;
      margin-bottom: 40px;
      color: #fff;
    }
    .section-content {
      max-width: 1000px;
      margin: 0 auto;
      text-align: center;
      font-size: 1.1rem;
      line-height: 1.8;
    }

    /* BOOKS SECTION */
    .books-container {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 40px;
      margin-top: 40px;
    }
    .book-card {
      background: #1e1e1e;
      border: 2px solid #7B68EE;
      border-radius: 10px;
      overflow: hidden;
      transition: transform 0.3s;
      display: flex;
      flex-direction: column;
      min-height: 600px; 
    }
    .book-card:hover {
      transform: scale(1.02);
    }
    .book-card img {
      width: 100%;
      height: 600px;
      object-fit: cover;
    }
    .book-card .book-details {
      padding: 20px;
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .book-card .book-details h3 {
      font-family: 'Cinzel', serif;
      font-size: 1.5rem;
      margin-bottom: 15px;
      color: #7B68EE;
    }
    .book-card .book-details p {
      flex: 1;
      margin-bottom: 20px;
    }
    .book-card .book-details a {
      padding: 10px 20px;
      border: 2px solid #7B68EE;
      color: #7B68EE;
      font-weight: 500;
      transition: background 0.3s, color 0.3s;
    }
    .book-card .book-details a:hover {
      background: #7B68EE;
      color: #fff;
    }


    /* GENRE TAGS */

    .genre-tags {
      display: flex;
      gap: 15px;
      margin-bottom: 20px;
    }

    .genre {
      font-size: 1rem;
      font-weight: 600;
      padding: 5px 10px;
      border-radius: 5px;
      color: #fff;
      transition: all 0.3s;
    }

    .genre.thriller {
      color: #FF6347; /
    }

    .genre.mystery {
      color: #4682B4; 
    }

    .genre.fantasy {
      color: #2E8B57; 
    }

    .genre.adventure {
      color: #DAA520; 
    }

    .genre:hover {
      opacity: 0.8;
    }


    /* FOOTER */
    footer {
      background: #1e1e1e;
      padding: 40px 20px;
      text-align: center;
      font-size: 0.9rem;
      color: #777;
    }
    footer a {
      color: #7B68EE;
    }
    footer a:hover {
      text-decoration: underline;
    }

    /* RESPONSIVENESS */
    @media (max-width: 768px) {
      header {
        padding: 20px;
      }
      header .brand {
        font-size: 1.5rem;
      }
       .menu-toggle {
        display: flex;
      }
      nav ul {
        flex-direction: column;
        position: absolute;
        top: 70px;
        left: 0;
        right: 0;
        background: #121212;
        display: none;
        padding: 10px 0;
      }
      nav ul.active {
        display: flex;
      }
      nav ul li {
        margin: 10px 0;
        text-align: center;
      }
      .hero h1 {
        font-size: 2.5rem;
      }
      .hero p {
        font-size: 1rem;
      }
      .section-title {
        font-size: 2rem;
      }
    }
  </style>
</head>
<body>

  <!-- HEADER / NAV -->
  <header>
    <div class="brand">Forsaken</div>
    <!-- Nav -->
    <nav>
      <ul id="nav-links">
        <li><a href="#hero">Home</a></li>
        <li><a href="#about">About</a></li>
        <li><a href="#books">Books</a></li>
        <li><a href="#lore">Lore</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
    </nav>
    <!-- Ham -->
    <div class="menu-toggle" id="menu-toggle">
      <span class="bar"></span>
      <span class="bar"></span>
      <span class="bar"></span>
    </div>
  </header>

  <!-- HERO SECTION -->
  <section class="hero" id="hero">
    <div class="hero-content">
      <h1>Welcome to Forsaken</h1>
      <p>"The mind is its own place, and in itself can make a heaven of hell, a hell of heaven." — John Milton.
        <br><br>
        Welcome to Forsaken, an archive of interconnected stories where everything against conventions is possible.
      </p>
      <a href="#books" class="btn">Explore Our Books</a>
    </div>
  </section>

  <!-- ABOUT SECTION -->
  <section id="about">
    <h2 class="section-title">About Us</h2>
    <div class="section-content">
      <p>
        We are the co-creators of the Forsaken universe. Our novels are anything from the limits of the ground, to the limits of the mind itself. In simpler terms? Everything.
      </p>
    </div>
  </section>

  <!-- BOOKS SECTION -->
  <section id="books">
    <h2 class="section-title">Our Books</h2>
    <div class="section-content">
      <p>Look into our collection of novels that rejects conventions and presents stories like no other.</p>
      <div class="books-container">
        <!-- Precedent Card -->
        <div class="book-card">
          <img src="precedent-bo.png" alt="Precedent Book Cover">
          <div class="book-details">
            <h3>Precedent</h3>
            <p>A psychological thriller where truth is not simply found – it is made.</p>
            <!-- Tags -->
            <div class="genre-tags">
              <span class="genre thriller">#Thriller</span>
              <span class="genre mystery">#Mystery</span>
            </div>
            <a href="https://docs.google.com/document/d/1mdJs3b1RtMPPuyWKEsBz3AZvvx5ogFun8zSVQV05jKE/edit?usp=sharing" target="_blank">Read More</a>
          </div>
        </div>

        <!-- Dual Lever Card -->
        <div class="book-card">
          <img src="duallever-bo.png" alt="Dual Lever Book Cover">
          <div class="book-details">
            <h3>Dual Lever</h3>
            <p>In a divided world, survival demands everything. This book takes this to further beyond.</p>
            <!-- Tags -->
            <div class="genre-tags">
              <span class="genre fantasy">#Fantasy</span>
              <span class="genre adventure">#Adventure</span>
            </div>
            <a href="https://docs.google.com/document/d/1n4PTjOlhDbLxG1RBpPak1CrLCBuOdJIKcRpG5SNyeeQ/edit?usp=sharing" target="_blank">Read More</a>
          </div>
        </div>


      </div>
    </div>
  </section>

  <!-- LORE SECTION -->
  <section id="lore">
    <h2 class="section-title">The Lore</h2>
    <div class="section-content">
      <p>
        The stories beyond what is presented, but certainly interesting. Everything leads to demise, and nothing leads to salvation. Manuals coming soon...
      </p>
    </div>
  </section>

  <!-- CONTACT SECTION -->
  <section id="contact">
    <h2 class="section-title">Contact Us</h2>
    <div class="section-content">
      <p>
        Have questions? Want to collaborate? Reach out at <a href="mailto:forsakenverse@tutamail.com">forsakenverse@tutamail.com</a> and join our little adventure. 
      </p>
    </div>
  </section>

  <!-- FOOTER -->
  <footer>
    <p>&copy; 2025 Forsaken. All rights reserved. | Designed with love for stories.</p>
  </footer>

  <!-- JS FOR HAM -->
  <script>
    const menuToggle = document.getElementById('menu-toggle');
    const navLinks = document.getElementById('nav-links');

    menuToggle.addEventListener('click', () => {
      navLinks.classList.toggle('active');
    });
  </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html_content)

if __name__ == "__main__":
    app.run(debug=True)
