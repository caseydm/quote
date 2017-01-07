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
});