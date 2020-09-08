//Run slick carousel
//By https://kenwheeler.github.io/slick/
$(document).ready(function () {
  $('#kc_logos').slick({
    mobileFirst: true,
    slidesToShow: 5,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 2000,
    centerMode: true,
    responsive: [{
        breakpoint: 1024,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 1,
          infinite: true,
          dots: true
        }
      },
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1
        }
      },
      {
        breakpoint: 376,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1
        }
      }
      // You can unslick at a given breakpoint now by adding:
      // settings: "unslick"
      // instead of a settings object
    ]
  });
});

function processAjaxData(response, urlPath) {
  document.getElementById("content").innerHTML = response.html;
  document.title = response.pageTitle;
  window.history.pushState({
    "html": response.html,
    "pageTitle": response.pageTitle
  }, "", urlPath);
}

// Get the container element
var btnContainer = document.getElementById("kc_navigation");

// Get all buttons with class="btn" inside the container
var btns = btnContainer.getElementsByTagName("a");

// Loop through the buttons and add the active class to the current/clicked button
for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function() {
    var current = document.getElementsByClassName("active");
    current[0].className = current[0].className.replace(" active", "");
    this.parentNode.className += " active";
  });
}

var urlArray = window.location.href.split("/");
var appPathName = urlArray[urlArray.length-2];
console.log(urlArray[urlArray.length-2]);
if (appPathName=="news"){
  btns[2].parentNode.className += " active";
} else if (appPathName=="donation"){
  btns[3].parentNode.className += " active";
} else if (appPathName=="contact-us"){
  btns[4].parentNode.className += " active";
} else if (appPathName=="recruitment"){
  btns[5].parentNode.className += " active";
} else{
  btns[0].parentNode.className += " active";
}