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
    $('.select').select2({
        minimumResultsForSearch: Infinity,
        width: 250,
        placeholder: "Select Client"
    });

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
            // success: function() {
            //     $("#content").append('<li>Task:' + data.title + ' Description:' + data.description + 'Status: false</li>');
            //     document.getElementById("taskForm").reset();
            //}
            success: function() {
                $('#add_client_modal').modal('hide')
            }
        });
    });

});