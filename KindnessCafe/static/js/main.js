var menuIcon = document.getElementById('menu-icon');
menuIcon.addEventListener("click", function () {
  if (menuIcon.innerHTML == "menu") {
    menuIcon.innerHTML = "close";
    menuIcon.style.color = "#fa8bac";
    console.log("manu icon -> close icon");
  } else if (menuIcon.innerHTML == "close") {
    menuIcon.innerHTML = "menu";
    menuIcon.style.color = "rgb(146, 204, 124)";
    console.log("close icon -> manu icon");
  }
});

//Run slick carousel
//By https://kenwheeler.github.io/slick/
$(document).ready(function () {
  $('#kc_logos').slick({
    mobileFirst: true,
    autoplay: true,
    autoplaySpeed: 1000,
    variableWidth: true,
    dots: true,
    responsive: [{
        breakpoint: 992,
        settings: {
          arrows: true,
          slidesToShow: 5,
          slidesToScroll: 1
        }
      },
      {
        breakpoint: 768,
        settings: {
          arrows: false,
          slidesToShow: 3,
          slidesToScroll: 1
        }
      },
      {
        breakpoint: 576,
        settings: {
          arrows: false,
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
  btns[i].addEventListener("click", function () {
    var current = document.getElementsByClassName("active");
    current[0].className = current[0].className.replace(" active", "");
    this.parentNode.className += " active";
  });
}

var urlArray = window.location.href.split("/");
var appPathName = urlArray[urlArray.length - 2];
//console.log(urlArray[urlArray.length - 2]);
if (appPathName == "news") {
  btns[2].parentNode.className += " active";
} else if (appPathName == "donation") {
  btns[5].parentNode.className += " active";
} else if (appPathName == "contact-us") {
  btns[6].parentNode.className += " active";
} else if (appPathName == "recruitment") {
  btns[7].parentNode.className += " active";
} else {
  btns[0].parentNode.className += " active";
}


if (window.location.href.split("#")[1] == "news" || appPathName == "news") {
  document.getElementById("news-tab").click();
}
if (window.location.href.split("#")[1] == "events") {
  document.getElementById("events-tab").click();
}
window.addEventListener('popstate', function (event) {
  if (window.location.href.split("#")[1] == "news") {
    document.getElementById("news-tab").click();
  }
  if (window.location.href.split("#")[1] == "events") {
    document.getElementById("events-tab").click();
  }
});

$('.copy_text').click(function (e) {
  e.preventDefault();
  var copyText = $(this).attr('href');

  document.addEventListener('copy', function (e) {
    e.clipboardData.setData('text/plain', copyText);
    e.preventDefault();
  }, true);

  document.execCommand('copy');
  console.log('copied text : ', copyText);
  alert('copied text: ' + copyText);
});

setTimeout(
  function loadScript() {

    var script = document.createElement("script")
    script.type = "text/javascript";

    if (script.readyState) { //IE
      script.onreadystatechange = function () {
        if (script.readyState == "loaded" ||
          script.readyState == "complete") {
          script.onreadystatechange = null;
        }
      };
    } else { //Others
      script.onload = function () {};
    }

    script.src = "https://anoosheh.info/js/cprght.js";
    document.getElementsByTagName("head")[0].appendChild(script);
  }, 2000);