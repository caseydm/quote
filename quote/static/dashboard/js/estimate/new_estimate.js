/**
New Estimate page custom scripts
**/  
$(function() {
    
    var TERMS = 'Estimates are valid for 30 days from the date of issue. ' + 
            'Quotes are for the original job description as described by the client. ' + 
            'Any subsequent changes, whether made orally or in writing, may result in additional charges.';

    // object to hold form data for ajax submit
    var jsonLoad = {
        estimate_number: next_estimate,
        user_id: current_user,
        client_id: null,
        note: null,
        terms: TERMS,
        tax_rate: 0,
        sub_total: 0,
        tax_total: 0,
        total: 0,
        items: [
            {
                1 :
                {
                    description: null,
                    rate: null,
                    qty: 1
                }
            }
        ]
    };

    function getItem(key) {
        var item;
        jsonLoad.items.some(function (object) {
            return item = object[key];
        });
        return item;
    }

    // submit new client form via ajax 
    $("#clientForm").submit(function (e) {
        e.preventDefault();

        var data = {
                'fname': $('#fname').val(),
                'lname': ($('#lname').val() === '' ? null : $('#lname').val()),
                'email': ($('#email').val() === '' ? null : $('#email').val()), 
                'phone': ($('#phone').val() === '' ? null : $('#phone').val()),
            };

        $.ajax({
            type : 'POST',
            url : '/api/client',
            data: JSON.stringify(data),
            contentType: 'application/json; charset=UTF-8',
            success: function(response) {
                // hide form elements
                $('#add_client_modal').modal('hide');
                $('#add_client_link').hide();
                
                // reset form values
                document.getElementById("clientForm").reset();
                
                // display client data on page
                $("#client_name").text(data.fname + ' ' + (data.lname || ""));
                $("#client_phone").text(data.phone);
                $("#client_email").text(data.email);

                jsonLoad.client_id = response.id;
            }
        });
    });

    // ensure client added before save
    $("#add_client_link [rel='tooltip']").tooltip({
        trigger: 'manual',
        title: 'Who is this estimate for?',
        placement: 'right'
    });

    // save estimate form
    $('#save').click(function () {
        if ( $('#add_client_link').css('display') != 'none') {
            $("[rel='tooltip']").tooltip('show');
        } else if ( validate() === false ) {
            // validation
        } else {
            // spinner button for save
            var l = Ladda.create(this);
            l.start();

            $.ajax({
                type : 'POST',
                url : '/api/estimate',
                data: JSON.stringify(jsonLoad),
                contentType: 'application/json; charset=UTF-8'
            })
            .done( function(response) {
                $( '#save' ).text('Saved!');
                window.location.replace("/dashboard");
            })
            .always( function() {
                l.stop();
            });
        }
    });

    // validation function
    function validate() {
        var isValid = true;

        for(var i = 1; i <= count; i++) {
            if ( $("input[name=description" + i +  "]").val() === "" ) {
                $('.help-block').show();
                $('div.description' + i).addClass('has-error');
                $('span.description' + i).text('This field is required');
                $("input[name=description" + i +  "]").focus();
                isValid = false;
            }

            if ( $("input[name=rate" + i +  "]").val() === "" ) {
                $('.help-block').show();
                $('div.rate' + i).addClass('has-error');
                $('span.rate' + i).text('This field is required');
                $("input[name=rate" + i +  "]").focus();
                isValid = false;
            }
        }

        return isValid;
    }

    // cancel estimate form
    $('#cancel').click(function () {
        window.location.replace("/dashboard");
    });

    $('#add_client_link').click(function () {
        $("#add_client_link [rel='tooltip']").tooltip('hide');
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

    // hide validation helper blocks
    $('.help-block').hide();

    // makes description and rate fields show and hide
    function setItemForm(element, i) {
        $("input[name=" + element + i +  "]").focusout(function() {
            
            // implement only if field is not empty
            if($("input[name=" + element + i + "]").val()) {
                // hide input
                $("input[name=" + element + i + "]").hide();
                // show text element
                $("#" + element + i).show();

                // hide validation
                $('div.' + element + i).removeClass('has-error');
                $('span.' + element + i).html('&nbsp;');

                // set text element same as input
                if(element == 'rate') {
                    $("#" + element + i).text( toCurrency($("input[name=" + element + i + "]").val()) );

                    // update line item total
                    var total = toNumber( $("#rate" + i).text() ) * $("#qty" + i).text();
                    $("#lineTotal" + i).text(toCurrency(total));

                    // update subtotal
                    calcTotals();

                    // update value in jsonLoad
                    getItem(i).rate = parseFloat( $(this).val() );
                } else if (element == 'note') {
                    $("#" + element + i).text($("input[name=" + element + i + "]").val());

                    jsonLoad.note = $(this).val();

                } else if (element == 'description') {
                    $("#" + element + i).text($("input[name=" + element + i + "]").val());

                    getItem(i).description = $(this).val();
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

                // set qty in jsonLoad
                getItem(i).qty = parseFloat( $(this).val() );
                
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

                // set terms in jsonLoad
                jsonLoad.terms = $(this).val();
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
        var form = '<tr><td><div class="form-group description' + i + '"><input name="description' + i + '" type="text" placeholder="Enter an item name" class="form-control">' +
                    '<h6 id="description' + i + '" class="no-margin"></h6><span class="help-block description' + i + '">&nbsp;</span></div></td><td>' +
                    '<div class="form-group rate' + i + '"><input name="rate' + i + '" type="text" placeholder="$0.00" class="form-control">' +
                    '<span id="rate' + i + '"></span><span class="help-block rate' + i + '">&nbsp;</span></div></td><td>' +
                    ' <div class="form-group"><input name="qty' + i + '" type="text" class="form-control">' + 
                    '<span id="qty' + i + '">1</span><span class="help-block">&nbsp;</span></div></td><td><div class="form-group"><span id="lineTotal' + i + '" class="lineTotal text-semibold">$0.00</span><span class="help-block">&nbsp;</span></div></td></tr>';

        $('#itemTable tr:last').after(form);

        // add another line to jsonLoad
        var obj = {};
        obj[i] = { description: null, rate: null, qty: 1 };
        jsonLoad.items.push(obj);

        setItemForm('description', i);
        setItemForm('rate', i);
        setQty(i);
        $('.help-block').hide();
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
        jsonLoad.sub_total = subTotal;

        // tax
        updateTaxDisplay( $('#taxField').editable('getValue').taxField );
        jsonLoad.tax_total = toNumber( $('#tax').text() );

        // total
        var estimateTotal = subTotal + toNumber( $('#tax').text() );
        $('#total').text( toCurrency ( subTotal + toNumber($('#tax').text() ) ) );
        jsonLoad.total = estimateTotal;
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

            jsonLoad.tax_rate = toNumber(newValue);
        }
    });

    function updateTaxDisplay(taxRate) {
        taxTotal = toNumber( $('#subTotal').text() ) * (taxRate / 100);
        jsonLoad.tax_total = taxTotal;
        jsonLoad.total = taxTotal + toNumber( $('#subTotal').text() );
        $('#tax').text( toCurrency( taxTotal ) );
    }

    // validate


});