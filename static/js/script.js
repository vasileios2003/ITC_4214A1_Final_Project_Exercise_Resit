function getCSRFToken() {
  const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]');
  return csrfToken ? csrfToken.value : '';
}

$(document).ready(function () {
  $('.star').on('click', function () {
    const score = $(this).data('value');
    const bookId = $('#rating-stars').data('book-id');

    $.post(`/rate/${bookId}/`, {
      score: score,
      csrfmiddlewaretoken: '{{ csrf_token }}'
    }).done(function (data) {
      alert(`Thank you! You rated this book ${data.new_score} stars.`);
    }).fail(function () {
      alert('Rating failed. Please try again.');
    });
  });
});

//Dark/light Mode //
$(document).ready(function () {
  const body = $("body");
  const toggleBtn = $("#darkModeToggle");

  if (localStorage.getItem("theme") === "dark") {
    body.removeClass("light-mode").addClass("dark-mode");
    toggleBtn.text("☀️");
  } else {
    body.removeClass("dark-mode").addClass("light-mode");
    toggleBtn.text("🌙");
  }

  toggleBtn.on("click", function () {
    body.toggleClass("dark-mode light-mode");
    const mode = body.hasClass("dark-mode") ? "dark" : "light";
    localStorage.setItem("theme", mode);
    toggleBtn.text(mode === "dark" ? "☀️" : "🌙");
  });
});

//slide show //
if (document.getElementsByClassName("mySlides").length > 0) {
  let slideIndex = 1;
  showSlides(slideIndex);

  window.plusSlides = function(n) {
    showSlides(slideIndex += n);
  }

  window.currentSlide = function(n) {
    showSlides(slideIndex = n);
  }

  function showSlides(n) {
    const slides = document.getElementsByClassName("mySlides");
    const dots = document.getElementsByClassName("dot");

    if (n > slides.length) { slideIndex = 1; }
    if (n < 1) { slideIndex = slides.length; }

    for (let i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
    }

    for (let i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
    }

    slides[slideIndex - 1].style.display = "block";
    dots[slideIndex - 1].className += " active";
  }
}
