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
    let team_id = $(this).prev();
    console.log(team_id);
    let team_1;
    let team_2;

    if (team_id === "away_team") {
        team_1 = team;
        team_2 = $("#home_team").text().trim();
    } else {
        team_2 = team;
        team_1 = $("#away_team").text().trim();
    }

    let betInfo = {
        team_1: team_1,
        team_2: team_2,
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
        const team_id = team[0].id;
        console.log(team_id);
        const team_name = team.text().trim();
        const betForm = $("#add_bet_form");
        const away_team = $(`<span id=${team_id}>Away</span>`);
        const home_team = $(`<span id=${team_id}>Home</span>`);
        betForm.show();

        const selectedBetPrice = $(this).parent().prev().find("b")[0].textContent;

        const betFormInput = $(".col-xs-1");
        betForm.before($(`<b>${team_name}</b>`));
        if (team_id === "away_team") {
            betForm.before(away_team);
        } else {
            betForm.before(home_team);
        }

        betFormInput.after(`<b>${selectedBetPrice}</b>`);
        betFormInput.after("<b> X </b>");
        $(".add_bet").hide();
    });
});

var triggerEl = document.querySelector('#myTab a[href="#profile"]');
bootstrap.Tab.getInstance(triggerEl).show(); // Select tab by name);
bootstrap.Tab.getInstance(triggerEl).show(); // Select tab by name