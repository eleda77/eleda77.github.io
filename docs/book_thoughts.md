---
layout: base
title: Book Thoughts
---
<style>
  .books-content-wrapper {
    width: 100%;
    clear: both;
    overflow: hidden;
    margin-bottom: 40px;
  }

  .reading-section {
    margin-bottom: 40px;
    clear: both;
  }

  .reading-section::after {
    content: "";
    display: table;
    clear: both;
  }
</style>

<div class="books-content-wrapper">
  <h1>Miscellaneous Book Thoughts</h1>
  <p>Some of my favourite books include:</p>
  <ul>
    <li><em>The Starless Sea</em> by Erin Morgenstern</li>
    <li><em>Ender's Game</em> by Orson Scott Card</li>
    <li><em>Dune</em> by Frank Herbert</li>
    <li>The <em>Three-Body Problem</em> trilogy by Cixin Liu</li>
    <li>The <em>Wayward Children</em> series by Seanan McGuire</li>
    <li>The <em>Harry Potter</em> series by J.K. Rowling (I don't support JKR's political beliefs)</li>
    <li>The <em>Discworld</em> series by Terry Pratchett</li>
    <li>The <em>Farseer</em> trilogy by Robin Hobb</li>
  </ul>

  {% include goodreads-styles.html %}
  
  <div class="reading-section">
    <h2>Goodreads Updates</h2>
    {% include currently-reading.html %}
  </div>

  <div class="reading-section">
    <h2>Recently Read</h2>
    {% include goodreads-grid.html %}
  </div>
</div>