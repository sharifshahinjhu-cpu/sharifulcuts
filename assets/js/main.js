// Md. Shariful Islam — shared site behavior (mobile nav, back-to-top, footer year, contact form)
(function () {
  "use strict";

  // Mobile nav toggle
  var toggle = document.getElementById("menu-toggle");
  var menu = document.getElementById("mobile-menu");
  var iconOpen = document.getElementById("menu-icon-open");
  var iconClose = document.getElementById("menu-icon-close");

  if (toggle && menu) {
    toggle.addEventListener("click", function () {
      var isHidden = menu.classList.contains("hidden");
      menu.classList.toggle("hidden");
      toggle.setAttribute("aria-expanded", isHidden ? "true" : "false");
      if (iconOpen && iconClose) {
        iconOpen.classList.toggle("hidden");
        iconClose.classList.toggle("hidden");
      }
    });

    // Close mobile menu when a link inside it is clicked
    menu.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        menu.classList.add("hidden");
        toggle.setAttribute("aria-expanded", "false");
        if (iconOpen && iconClose) {
          iconOpen.classList.remove("hidden");
          iconClose.classList.add("hidden");
        }
      });
    });
  }

  // Back to top
  var backToTop = document.getElementById("back-to-top");
  if (backToTop) {
    backToTop.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  // Footer year
  var yearEl = document.getElementById("year");
  if (yearEl) {
    yearEl.textContent = new Date().getFullYear();
  }

  // Pre-fill contact form when arriving from a shop.html "package"/"product" link
  var interestField = document.getElementById("interest");
  var messageField = document.getElementById("message");
  if (interestField && messageField) {
    var params = new URLSearchParams(window.location.search);
    var slug = params.get("package") || params.get("product");
    if (slug) {
      var labels = {
        "starter-cut": "Starter Cut package",
        "agency-partnership": "Agency Partnership package",
        "cinematic-color-lut-pack": "Cinematic Color LUT Pack",
        "multilingual-motivational-script-pack": "Multilingual Motivational Script Pack",
        "reflection-music-vol.-1": "Reflection Music Vol. 1"
      };
      var label = labels[slug] || slug.replace(/-/g, " ");

      for (var i = 0; i < interestField.options.length; i++) {
        if (interestField.options[i].text.indexOf("Shop") === 0) {
          interestField.selectedIndex = i;
          break;
        }
      }
      if (!messageField.value.trim()) {
        messageField.value = "I'm interested in: " + label + "\n\n";
      }
    }
  }

  // Contact form -> mailto (no backend required)
  var form = document.getElementById("contact-form");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var name = form.querySelector("#name").value.trim();
      var email = form.querySelector("#email").value.trim();
      var interest = form.querySelector("#interest").value;
      var message = form.querySelector("#message").value.trim();

      var subject = "New inquiry: " + interest;
      var body =
        "Name: " + name + "\n" +
        "Email: " + email + "\n" +
        "Interest: " + interest + "\n\n" +
        message;

      var mailto =
        "mailto:sharifshahin.jhu@gmail.com" +
        "?subject=" + encodeURIComponent(subject) +
        "&body=" + encodeURIComponent(body);

      window.location.href = mailto;

      var fallback = document.getElementById("contact-fallback");
      if (fallback) {
        fallback.classList.remove("hidden");
      }
    });
  }
})();
