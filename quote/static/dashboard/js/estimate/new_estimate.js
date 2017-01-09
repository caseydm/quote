/* ------------------------------------------------------------------------------
*
*  # Editable component
*
*  Specific JS code additions for form_editable.html page
*
*  Version: 1.1
*  Latest update: Mar 5, 2016
*
* ---------------------------------------------------------------------------- */

$(function() {
    // Default initialization
    // $('.select').select2({
    //     minimumResultsForSearch: Infinity,
    //     width: 250,
    //     placeholder: "Select Client"
    // });

    // Submit client
    $("#clientForm").submit(function (e) {
        e.preventDefault();

        var data = {
                'fname': $('#fname').val(),
                'lname': $('#lname').val(),
                'email': $('#email').val(),
                'phone': $('#phone').val(),
            };

        $.ajax({
            type : 'POST',
            url : '/api/client',
            data: JSON.stringify(data),
            contentType: 'application/json; charset=UTF-8',
            success: function() {
                $('#add_client_modal').modal('hide');
                $('#add_client_link').hide();
                document.getElementById("clientForm").reset();
                $("#client_name").text(data.fname + ' ' + data.lname);
                $("#client_phone").text(data.phone);
                $("#client_email").text(data.email);
            }
        });
    });

});