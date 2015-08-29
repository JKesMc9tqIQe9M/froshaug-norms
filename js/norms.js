$(function() {

    var ROW_REVEAL_INTERVAL = 55;

    var INTERVAL_ID = window.setInterval(revealRows, ROW_REVEAL_INTERVAL);

    function revealRows() {
        var $trs = $(".unpopulated");
        if (!$trs.length) {
            window.clearInterval(INTERVAL_ID);
            return;
        }
        $trs.first()
            .removeClass("unpopulated")
            .find(".quad")
            .show()
            .addClass("animated rotateInDownLeft");
    };

});