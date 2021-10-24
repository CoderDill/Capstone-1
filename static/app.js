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
    $("#no_bets").hide();

    const team = $(this).parent().prev().prev();
    console.log(team);
    const $team = team[0].id;
    console.log($team);
    let homeTeam;
    let awayTeam;
    if ($team === "away_team") {
      homeTeam = team.parent().next().children("#home_team").text().trim();
      console.log(homeTeam);
      awayTeam = team.text().trim();
      console.log(awayTeam);
    } else {
      homeTeam = team.text().trim();
      awayTeam = team.parent().prev().children("#away_team").text().trim();
    }

    const teamToBet = team.text().trim();
    const $teamName = $("<b>").attr("class", "team_to_bet").text(teamToBet);
    const betForm = $("#add_bet_form");

    betForm.show();
    const selectedBetPrice = $(this).parent().prev().find("b")[0].textContent;

    $("#hidden").val([awayTeam, homeTeam, selectedBetPrice, $teamName]);

    const betFormInput = $(".col-xs-1");

    betForm.before($teamName);
    betFormInput.after(
      `<b id="bet_odds" name=${selectedBetPrice} value=${selectedBetPrice}>${selectedBetPrice}</b>`
    );
    betFormInput.after("<b class='X'> X </b>");
    $(".add_bet").hide();
  });
});

$("#cancel_bet").click(function () {
  $("#add_bet_form").hide();
  $(".team_to_bet").hide();
  $("#bet_odds").hide();
  $(".X").hide();
  $(".add_bet").show();
});
var triggerEl = document.querySelector('#myTab a[href="#upcoming"]');
bootstrap.Tab.getInstance(triggerEl).show(); // Select tab by name);
