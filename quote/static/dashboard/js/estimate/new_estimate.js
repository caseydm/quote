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

    // add item form

    // first item counter
    var count = 1;

    // initiliaze form
    setItemForm('description', count);
    setItemForm('rate', count);
    setQty(count);

    function setItemForm(element, i) {
        $("input[name=" + element + i +  "]").focusout(function() {
            if($("input[name=" + element + i + "]").val()) { 
                $("input[name=" + element + i + "]").hide();
                $("#" + element + i).show();
                $("#" + element + i).text($("input[name=" + element + i + "]").val());
            }
        });

        $("#" + element + i).click(function() {
            $("input[name=" + element + i + "]").show().focus();
            $("#" + element + i).hide();
        });
    }

    function setQty(i) {
        $("input[name=qty" + i + "]").hide();

        $("input[name=qty" + i + "]").focusout(function() {
            if($("input[name=qty" + i + "]").val()) {
                $("input[name=qty" + i + "]").hide();
                $('#qty' + i).show();
                $('#qty' + i).text($("input[name=qty" + i + "]").val());
            }
        });

        $('#qty' + i).click(function() {
            $("input[name=qty" + i + "]").val($('#qty' + i).text());
            $("input[name=qty" + i + "]").show().focus();
            $('#qty' + i).hide();
        });
    }

    // add an item row
    $("#addRow").click(function() {
        count += 1;
        addRow(count);
    });

    function addRow(i) {
        console.log(i);
        
        var form = '<tr><td><input name="description' + i + '" type="text" placeholder="Enter an item name" class="form-control">' +
                    '<h6 id="description' + i + '" class="no-margin"></h6></td><td>' +
                    '<input name="rate' + i + '" type="text" class="form-control">' +
                    '<span id="rate' + i + '"></span></td><td>' +
                    '<input name="qty' + i + '" type="text" class="form-control">' + 
                    '<span id="qty' + i + '">1</span></td><td><span class="text-semibold">$0.00</span></td></tr>'

        $('#itemTable tr:last').after(form);

        setItemForm('description', i);
        setItemForm('rate', i);
        setQty(i);
    }

});