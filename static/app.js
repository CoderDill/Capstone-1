// bootstrap trigger tab list
var triggerTabList = [].slice.call(document.querySelectorAll("#myTab a"));
triggerTabList.forEach(function (triggerEl) {
  var tabTrigger = new bootstrap.Tab(triggerEl);

  triggerEl.addEventListener("click", function (event) {
    event.preventDefault();
    tabTrigger.show();
  });
});

// add a click evt to each bet's + symbol
$(".add_bet").each(function (event) {
  $(this).on("click", function (event) {
    event.preventDefault();
    $("#no_bets").hide();

    // Get Home/Away teams for game
    const team = $(this).parent().prev().prev();
    const $team = team[0].id;

    let homeTeam;
    let awayTeam;
    if ($team === "away_team") {
      homeTeam = team.parent().next().children("#home_team").text().trim();
      awayTeam = team.text().trim();
    } else {
      homeTeam = team.text().trim();
      awayTeam = team.parent().prev().children("#away_team").text().trim();
    }

    // Get users team, show the form to submit bet, add needed backend data to a hidden tag that submits with form.
    const teamToBet = team.text().trim();
    const $teamName = $("<b>").attr("class", "team_to_bet").text(teamToBet);
    const betForm = $("#add_bet_form");
    betForm.show();
    const selectedBetPrice = $(this).parent().prev().find("b")[0].textContent;

    $("#hidden").val([awayTeam, homeTeam, selectedBetPrice, teamToBet]);

    const betFormInput = $(".col-xs-1");

    betForm.before($teamName);
    betFormInput.after(
      `<b id="bet_odds" name=${selectedBetPrice} value=${selectedBetPrice}>${selectedBetPrice}</b>`
    );
    betFormInput.after("<b class='X'> X </b>");
    $(".add_bet").hide();
  });
});

// if there are not games for a section, show message.
const upcoming = $("#upcoming");
const nfl = $("#nfl");
const mlb = $("#mlb");
const mma = $("#mma");

if (upcoming.children().text().trim() == "") {
  upcoming.prepend(
    "<h1 class='font-weight-bold m-2'>No upcoming bets at this time.</h1>"
  );
}
if (nfl.children().text().trim() == "") {
  nfl.prepend(
    "<h1 class='font-weight-bold m-2'>No NFL bets at this time.</h1>"
  );
}
if (mlb.children().text().trim() == "") {
  mlb.prepend(
    "<h1 class='font-weight-bold m-2'>No MLB bets at this time.</h1>"
  );
}
if (mma.children().text().trim() == "") {
  mma.prepend(
    "<h1 class='font-weight-bold m-2'>No MMA bets at this time.</h1>"
  );
}

$(".show_result_form").each(function (event) {
  $(this).on("click", function (event) {
    event.preventDefault();

    const $form = $(this).prev().prev();
    $form.show();
    const bet_id = $form
      .parent()
      .parent()
      .parent()
      .children("#bet_id")
      .attr("value");
    $form.children("#hidden_result").val(bet_id);
    $(this).hide();
    $(this).prev().hide();
  });
});

// Cancel bet btn hides bet form
$("#cancel_bet").click(function () {
  $("#add_bet_form").hide();
  $(".team_to_bet").hide();
  $("#bet_odds").hide();
  $(".X").hide();
  $(".add_bet").show();
});

// Tabs between Sports
var triggerEl = document.querySelector('#myTab a[href="#upcoming"]');
bootstrap.Tab.getInstance(triggerEl).show(); // Select tab by name);
