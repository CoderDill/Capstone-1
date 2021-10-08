var triggerTabList = [].slice.call(document.querySelectorAll("#myTab a"));
triggerTabList.forEach(function(triggerEl) {
    var tabTrigger = new bootstrap.Tab(triggerEl);

    triggerEl.addEventListener("click", function(event) {
        event.preventDefault();
        tabTrigger.show();
    });
});

$("#add_bet_form").submit(function(event) {
    event.preventDefault();
    console.log("submitted");
    let $team = $(this).prev();
    console.log($team);
    let team1;
    let team2;

    if ($team[0].id === "bet_away_team") {
        team1 = $team[0].textContent;
        team2 = $("#bet_home_team").text().trim();
    } else if ($team[0].id === "bet_home_team") {
        team1 = $("#bet_away_team").text().trim();
        team2 = $team[0].innerText;
    }

    let betInfo = {
        team_1: team1,
        team_2: team2,
    };

    let betArray = JSON.stringify(betInfo);

    $.ajax({
        type: "POST",
        url: "/add_bet",
        data: betArray,
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function(results) {
            console.log(results);
        },
    });
});

$(".add_bet").each(function(event) {
    $(this).on("click", function(event) {
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
            awayTeam = team
                .parent()
                .previous()
                .children("#away_team")
                .text()
                .trim();
        }

        const teamName = team.text().trim();
        const $teamName = $("<b>").text(teamName);
        const betForm = $("#add_bet_form");

        betForm.show();

        const selectedBetPrice = $(this).parent().prev().find("b")[0].textContent;

        const betFormInput = $(".col-xs-1");

        betForm.before($teamName);
        betFormInput.after(`<b>${selectedBetPrice}</b>`);
        betFormInput.after("<b> X </b>");
        $(".add_bet").hide();
    });
});

var triggerEl = document.querySelector('#myTab a[href="#profile"]');
bootstrap.Tab.getInstance(triggerEl).show(); // Select tab by name);
bootstrap.Tab.getInstance(triggerEl).show(); // Select tab by name