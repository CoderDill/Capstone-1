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
    const betForm = $(".add_bet_form");
    let selectedBetPrice = $(this).parent().prev().find("b")[0].textContent;
    let teamName = $(this).parent().prev().prev().text();
    betForm.show();
    betForm.after(`${teamName} x ${selectedBetPrice}`);
    console.log(teamName);
  });
});

var triggerEl = document.querySelector('#myTab a[href="#profile"]');
bootstrap.Tab.getInstance(triggerEl).show(); // Select tab by name
