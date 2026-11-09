// Md. Shariful Islam — site behaviour: mobile menu, sample autoplay, footer year.
(function () {
  "use strict";

  // Mobile menu
  var btn = document.getElementById("menu-btn");
  var menu = document.getElementById("mobile-menu");
  if (btn && menu) {
    btn.addEventListener("click", function () {
      var open = menu.classList.toggle("open");
      btn.setAttribute("aria-expanded", open ? "true" : "false");
    });
    menu.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () {
        menu.classList.remove("open");
        btn.setAttribute("aria-expanded", "false");
      });
    });
  }

  // Footer year
  var y = document.getElementById("year");
  if (y) y.textContent = new Date().getFullYear();

  // Sample videos: click-to-load. Nothing is requested from YouTube until the viewer presses play.
  function embedUrl(id) {
    var p = ["autoplay=1", "controls=1", "playsinline=1", "rel=0", "modestbranding=1"];
    return "https://www.youtube-nocookie.com/embed/" + encodeURIComponent(id) + "?" + p.join("&");
  }

  function mount(box) {
    if (box.querySelector("iframe")) return;
    var f = document.createElement("iframe");
    f.src = embedUrl(box.getAttribute("data-yt"));
    f.title = box.getAttribute("data-title") || "Sample video";
    f.allow = "autoplay; encrypted-media; picture-in-picture; fullscreen";
    f.allowFullscreen = true;
    f.referrerPolicy = "strict-origin-when-cross-origin";
    box.appendChild(f);
    var poster = box.querySelector(".poster");
    if (poster) poster.style.display = "none";
  }

  document.querySelectorAll(".sample[data-yt]").forEach(function (box) {
    var b = box.querySelector(".play");
    if (b) b.addEventListener("click", function () { mount(box); });
  });
})();
