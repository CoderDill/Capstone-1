var triggerTabList = [].slice.call(document.querySelectorAll("#myTab a"));
triggerTabList.forEach(function (triggerEl) {
  var tabTrigger = new bootstrap.Tab(triggerEl);

  triggerEl.addEventListener("click", function (event) {
    event.preventDefault();
    tabTrigger.show();
  });
});

$("#add_bet").each(function (event) {
  $(self).on("click", function (event) {
    event.preventDefault();
    console.log("here's the event-----", event.target);
  });
});

var triggerEl = document.querySelector('#myTab a[href="#profile"]');
bootstrap.Tab.getInstance(triggerEl).show(); // Select tab by name

// var triggerFirstTabEl = document.querySelector("#myTab li:first-child a");
// bootstrap.Tab.getInstance(triggerFirstTabEl).show(); // Select first tab
