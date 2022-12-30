



function timeStringToFloat(time) {
    var hoursMinutes = time.split(/[.:]/);
    var hours = parseInt(hoursMinutes[0], 10);
    var minutes = hoursMinutes[1] ? parseInt(hoursMinutes[1], 10) : 0;
    return hours + minutes / 60;
  }

function total_hobbs_time() {
    var start_time = $("#hobbs_start").val();
    var end_time = $("#hobbs_end").val();

    if (start_time == "" || end_time == "") {
        $("#hobbs_total").val("");
    }

    var total_time = end_time - start_time;
    if (total_time < 0) {
        return;
    }
    $("#hobbs_total").val(total_time.toFixed(2));
}

function total_ground_time() {
    var start_time = $("#ground_start").val();
    var end_time = $("#ground_end").val();

    if (start_time == "" || end_time == "") {
        $("#ground_total").val("");
    }

    var total_time = timeStringToFloat(end_time) - timeStringToFloat(start_time);
    if (total_time < 0) {
        $("#ground_total").val(0);
        return;
    }
    $("#ground_total").val(total_time.toFixed(2));
}

//Use Jquery to get value of the input field by id on change event of either input fields
$(document).ready(function() {
    console.log("SCRIPT LOADED");



    $("#hobbs_end").change(function() {
        total_hobbs_time();
    });

    $("#hobbs_start").change(function() {
        total_hobbs_time();
    });

    $("#ground_start").change(function() {
        total_ground_time();
    });

    $("#ground_end").change(function() {
        total_ground_time();
    });




});
