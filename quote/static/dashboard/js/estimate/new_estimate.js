/**
New Estimate page custom scripts
**/  
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

    /**
    Add item form
    **/  

    // first item counter
    var count = 1;

    // initiliaze form
    setItemForm('description', count);
    setItemForm('rate', count);
    setItemForm('note', count);
    setQty(count);
    setTerms();

    // makes description and rate fields show and hide
    function setItemForm(element, i) {
        $("input[name=" + element + i +  "]").focusout(function() {
            
            // implement only if field is not empty
            if($("input[name=" + element + i + "]").val()) {
                // hide input
                $("input[name=" + element + i + "]").hide();
                // show text element
                $("#" + element + i).show();
                // set text element same as input
                if(element == 'rate') {
                    $("#" + element + i).text( toCurrency($("input[name=" + element + i + "]").val()) );

                    // update line item total
                    var total = toNumber( $("#rate" + i).text() ) * $("#qty" + i).text();
                    $("#lineTotal" + i).text(toCurrency(total));

                    // update subtotal
                    calcTotals();
                } else {
                    $("#" + element + i).text($("input[name=" + element + i + "]").val());
                }
            }
        });

        $("#" + element + i).click(function() {
            // show input and hide text
            $("input[name=" + element + i + "]").show().focus();
            $("#" + element + i).hide();
        });
    }

    // set quantity field
    function setQty(i) {
        $("input[name=qty" + i + "]").hide();

        $("input[name=qty" + i + "]").focusout(function() {
            if($("input[name=qty" + i + "]").val()) {
                $('.error').remove();
                $("input[name=qty" + i + "]").hide();
                $('#qty' + i).show();
                $('#qty' + i).text($("input[name=qty" + i + "]").val());
                
                // update line item total
                var total = toNumber( $("#rate" + i).text() ) * $("#qty" + i).text();
                $("#lineTotal" + i).text(toCurrency(total));

                // update subtotal
                calcTotals();
            }
        });

        $('#qty' + i).click(function() {
            $("input[name=qty" + i + "]").val($('#qty' + i).text());
            $("input[name=qty" + i + "]").show().focus();
            $('#qty' + i).hide();
        });
    }

    function setTerms() {// set terms
        $('textarea[name="terms"]').hide();

        $("#terms").click(function() {
            // hide text and reveal input
            $('textarea[name="terms"]').val($('#terms').text());
            $('textarea[name="terms"]').show().focus();
            $('#terms').hide();
        });

        $('textarea[name="terms"]').focusout(function() {
            if($('textarea[name="terms"]').val()) {
                $('textarea[name="terms"]').hide();
                $('#terms').show();
                $('#terms').text($('textarea[name="terms"]').val());
            }
        });
    }


    /**
    Add a new item row
    **/  
    $("#addRow").click(function() {
        count += 1;
        addRow(count);
    });

    function addRow(i) {
        var form = '<tr><td><input name="description' + i + '" type="text" placeholder="Enter an item name" class="form-control">' +
                    '<h6 id="description' + i + '" class="no-margin"></h6></td><td>' +
                    '<input name="rate' + i + '" type="text" placeholder="$0.00" class="form-control">' +
                    '<span id="rate' + i + '"></span></td><td>' +
                    '<input name="qty' + i + '" type="text" class="form-control">' + 
                    '<span id="qty' + i + '">1</span></td><td><span id="lineTotal' + i + '" class="lineTotal text-semibold">$0.00</span></td></tr>'

        $('#itemTable tr:last').after(form);

        setItemForm('description', i);
        setItemForm('rate', i);
        setQty(i);
    }
    /**
    Utilities
    **/  

    // format currency
    function toCurrency(number) {
        var currency = '$' + parseFloat(number, 10).toFixed(2).replace(/(\d)(?=(\d{3})+\.)/g, "$1,").toString();
        return currency;
    }

    function toNumber(currency) {
        var number = Number(currency.replace(/[^0-9\.]+/g,""));
        return number;
    }

    // calculate and display subTotal, tax, and total
    function calcTotals() {
        
        // add line items
        var subTotal = 0;
        $('.lineTotal').each(function(i, obj) {
            subTotal += toNumber( $(this).text() ) || 0;
        });

        // subTotal
        $('#subTotal').text( toCurrency( subTotal ) );

        // tax
        updateTaxDisplay( $('#taxField').editable('getValue').taxField );

        // total
        $('#total').text( toCurrency ( subTotal + toNumber($('#tax').text() ) ));
    }

    // tax field

    $('#taxField').editable({
        placement: 'left',
        value: 0,
        inputclass: 'width-100',
        source: [
            {value: 0, text: '0%'},
            {value: 1, text: '1%'},
            {value: 2, text: '2%'},
            {value: 3, text: '3%'},
            {value: 4, text: '4%'},
            {value: 5, text: '5%'},
            {value: 6, text: '6%'},
            {value: 7, text: '7%'},
            {value: 8, text: '8%'},
            {value: 9, text: '9%'},
            {value: 10, text: '10%'}
        ],
        success: function(response, newValue) {
            updateTaxDisplay(newValue);
            $('#total').text( toCurrency ( toNumber( $('#subTotal').text() ) + toNumber($('#tax').text() ) ));
        }
    });

    function updateTaxDisplay(taxRate) {
        taxTotal = toNumber( $('#subTotal').text() ) * (taxRate / 100);
        $('#tax').text( toCurrency( taxTotal ) );
    }

    // // validation
    // var validator = $("#newEstimateForm").validate({
    //     onfocusout: false,
    //     debug: true,
    //     success: function(label,element) {
    //         label.parent().removeClass('error');
    //         label.remove(); 
    //     }
    // });

});