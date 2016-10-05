/**
 * Created by Agustin on 10/2/16.
 */


// TIMMER JS --------------------
var delay = (function () {
    var timer = 0;
    return function (callback, ms) {
        clearTimeout(timer);
        timer = setTimeout(callback, ms);
    };
})();


function getItems(searchTerm) {
    $.ajax({
        url: "/catalog/itemlist/",
        method: 'GET',
        data: {search_term: searchTerm},
        context: document.body
    }).done(function (item_list) {
        $('#products').html(item_list);
    });
}

// Searchbar timer in order to hold the call until the user stops typing for x ms
// Assigns timer to the search function
$('#item-search-input').keyup(function () {
    var searchTerm = event.target.value;
    delay(function () {
        getItems(searchTerm);
    }, 500);
});


