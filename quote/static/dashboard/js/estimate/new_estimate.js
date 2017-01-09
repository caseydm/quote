// new estimate custom scripts

$(function() {
    // submit new client form via ajax 
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
                // hide form elements
                $('#add_client_modal').modal('hide');
                $('#add_client_link').hide();
                
                // reset form values
                document.getElementById("clientForm").reset();
                
                // display client data on page
                $("#client_name").text(data.fname + ' ' + data.lname);
                $("#client_phone").text(data.phone);
                $("#client_email").text(data.email);
            }
        });
    });

});