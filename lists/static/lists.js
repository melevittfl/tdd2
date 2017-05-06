/**
 * Created by mlevitt on 06/05/2017.
 */
window.Superlists  = {};
window.Superlists.initialize = function() {
    $('input[name="text"]').on('keypress', function() {
        $('.has-error').hide();
    });
};
