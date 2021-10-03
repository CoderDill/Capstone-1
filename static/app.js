var triggerTabList = [].slice.call(document.querySelectorAll("#myTab a"));
triggerTabList.forEach(function(triggerEl) {
    var tabTrigger = new bootstrap.Tab(triggerEl);

    triggerEl.addEventListener("click", function(event) {
        event.preventDefault();
        tabTrigger.show();
    });
});

$(".add_bet").each(function(event) {
    $(this).on("click", function(event) {
        event.preventDefault();

        const betForm = $("#add_bet_form");
        betForm.show();
        let team = $(this).parent().prev().prev().text().trim();
        let team_id = $(this).parent().prev().prev().attr("id");
        let team_1;
        let team_2;

        if (team_id === "away_team") {
            team_1 = team;
            team_2 = $("#home_team").text().trim();
        } else {
            team_2 = team;
            team_1 = $("#away_team").text().trim();
        }

        const selectedBetPrice = $(this).parent().prev().find("b")[0].textContent;

        const betFormInput = $(".col-xs-1");
        betForm.before(`<b>${team_1}</b>`);
        betFormInput.after(`<b>${selectedBetPrice}</b>`);
        betFormInput.after("<b> X </b>");

        let betInfo = {
            team_1: team_1,
            team_2: team_2,
        };

        let betArray = JSON.stringify(betInfo);

        $.ajax({
            type: "POST",
            url: "/add_bet",
            data: betArray,
            contentType: "application/json",
            dataType: "json",
            success: function(results) {
                console.log(results.data);
            },
        });
    });
});

var triggerEl = document.querySelector('#myTab a[href="#profile"]');
bootstrap.Tab.getInstance(triggerEl).show(); // Select tab by name);
bootstrap.Tab.getInstance(triggerEl).show(); // Select tab by name