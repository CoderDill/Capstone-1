var triggerTabList = [].slice.call(document.querySelectorAll("#myTab a"));
triggerTabList.forEach(function (triggerEl) {
  var tabTrigger = new bootstrap.Tab(triggerEl);

  triggerEl.addEventListener("click", function (event) {
    event.preventDefault();
    tabTrigger.show();
  });
});

// $("#add_bet_form").submit(function (event) {
//   const teams = $(this).attr("data-teams");
//   const teamsArray = teams.split(",");

//   let betInfo = {
//     team_1: teamsArray[0],
//     team_2: teamsArray[1],
//   };

//   let betArray = JSON.stringify(betInfo);

//   $.ajax({
//     type: "POST",
//     url: "/add_bet",
//     data: betArray,
//     contentType: "application/json; charset=utf-8",
//     dataType: "json",
//     success: function (results) {
//       console.log(results);
//     },
//   });
// });

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
    $("#hidden").val([awayTeam, homeTeam]);
    const selectedBetPrice = $(this).parent().prev().find("b")[0].textContent;

    const betFormInput = $(".col-xs-1");

    betForm.before($teamName);
    betFormInput.after(`<b class="bet_price">${selectedBetPrice}</b>`);
    betFormInput.after("<b class='X'> X </b>");
    $(".add_bet").hide();
  });
});

$("#cancel_bet").click(function () {
  $("#add_bet_form").hide();
  $(".team_to_bet").hide();
  $(".bet_price").hide();
  $(".X").hide();
  $(".add_bet").show();
});
var triggerEl = document.querySelector('#myTab a[href="#profile"]');
bootstrap.Tab.getInstance(triggerEl).show(); // Select tab by name);
bootstrap.Tab.getInstance(triggerEl).show(); // Select tab by name
