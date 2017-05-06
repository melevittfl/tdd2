/**
 * Created by mlevitt on 06/05/2017.
 */
var initialize = function() {
    $('input[name="text"]').on('keypress', function() {
        $('.has-error').hide();
    });
};
