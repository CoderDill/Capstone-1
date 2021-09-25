var triggerTabList = [].slice.call(document.querySelectorAll("#myTab a"));
triggerTabList.forEach(function (triggerEl) {
  var tabTrigger = new bootstrap.Tab(triggerEl);

  triggerEl.addEventListener("click", function (event) {
    event.preventDefault();
    tabTrigger.show();
  });
});

$(".add_bet").each(function (event) {
  $(this).on("click", function (event) {
    event.preventDefault();
    let selectedBetPrice = $(this).parent().prev().find("b")[0].textContent;
  });
});

var triggerEl = document.querySelector('#myTab a[href="#profile"]');
bootstrap.Tab.getInstance(triggerEl).show(); // Select tab by name

// var triggerFirstTabEl = document.querySelector("#myTab li:first-child a");
// bootstrap.Tab.getInstance(triggerFirstTabEl).show(); // Select first tab
