/**
Dashboard custom scripts
**/  
$(function() {
    if(initial_setup !== 'True') {
        $('#business_setup_modal').modal('show');
    }

    // submit business info via ajax 
    $("#businessForm").submit(function (e) {
        e.preventDefault();

        var data = {
                'fname': $('#fname').val(),
                'lname': $('#lname').val(),
                'business_name': $('#business_name').val(),
                'phone': $('#phone').val(),
            };

        $.ajax({
            type : 'POST',
            url : '/api/business_setup',
            data: JSON.stringify(data),
            contentType: 'application/json; charset=UTF-8',
            success: function(response) {
                // hide form elements
                $('#business_setup_modal').modal('hide');
                
                // display on page
                $("#username").text(data.fname);
            }
        });
    });
});