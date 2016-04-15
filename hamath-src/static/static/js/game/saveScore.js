(function saveScore(){
	var mode = "rookie";
	var URL = mode + "_mode";
    var score = {mode : 25}; // mode and score are hardcoded for the sake of example
    $.post(URL, score, function(data,status){
        // if (status==="success") { alert("your score of " + score + " was saved." } );
        // else { alert("Sorry but your score was not saved.\nStatus: " + status }
    });
})();