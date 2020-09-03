
    const countUp = new CountUp('targetId', 5234);
if (!countUp.error) {
  countUp.start();
} else {
  console.error(countUp.error);
}

var values = document.querySelectorAll('.value');

[].forEach.call(values, function(h5) {
  // do whatever
  div.style.color = "red";
});
