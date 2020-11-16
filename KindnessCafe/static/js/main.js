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


/* FOOTER SECTION */
function scrollToValue() {
    window.scrollBy(0, 1000);
}

function copyrightAppend() {
    currentYear = new Date().getFullYear()
    var copyright = '';
    copyright += '<div id="copyright" class="my-2">' +
        '<div class="navbar-collapse collapse" id="copyrightButton">' +
        '<div class="navbar-nav mx-auto my-auto">' +
        '<div class="row">' +
        '<div class="col-xl-6 col-lg-6 col-md-12 col-sm-12 my-3">' +
        '<a class="border border-org px-1 py-1 mx-1" href="https://www.linkedin.com/in/imananoosheh">Iman Anooshehpour</a>' +
        '</div>' +
        '<div class="col-xl-6 col-lg-6 col-md-12 col-sm-12 my-3">' +
        '<a class="border border-org px-1 py-1 mx-1" href="https://www.linkedin.com/in/masoudsadeghi1996">Masoud Sadeghi</a>' +
        '</div>' +
        '</div>' +
        '</div>' +
        '</div>' +
        '<span>| Designed & Developed by  </span>' +
        '<button id="copyright-button" class="border border-org navbar-toggler collapsed" type="button" data-toggle="collapse" data-target="#copyrightButton" aria-controls="copyrightButton" aria-expanded="false" aria-label="Toggle navigation" data-placement="top">' +
        'Team 0x0' +
        '</button>' +
        '<span>  © ' + currentYear + ' | All rights reserved. |</span>' +
        '</div>';


    $("footer").after(copyright);
}

copyrightAppend();

document.getElementById('copyright-button').addEventListener("click", function () {
    setTimeout(function () {
        window.scrollBy(0, 100);
    }, 200);
});
/* END OF FOOTER SECTION */


/* GOTOTOP BUTTON SECTION */
//Go to the Top Button
// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () {
  scrollFunction()
};

function scrollFunction() {
  if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
    document.getElementById("gototopbtn").style.display = "block";
  } else {
    document.getElementById("gototopbtn").style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  $("html, body").animate({ scrollTop: 0 }, 600);
  //document.body.scrollTop = 0;
  //document.documentElement.scrollTop = 0;
}

document.getElementById('gototopbtn').addEventListener("click", function () {
    topFunction();
});
/* END GOTOTOP BUTTON SECTION */
