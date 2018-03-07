$(document).ready(function() {

    // Clicking table row opens item detail view page
    $(".clickable-cell").click(function() {
        window.location = $(this).data("href");
    });

    // AJAX call for adding item to cart
    $('.add-to-cart-button').click(function() {
        fetch("/store/item/" + $(this).attr("value") + "/add_to_cart", {
            credentials: "same-origin"
        })
        .then((response) => {
            if(response.ok) {
                return response;
            }
            throw new Error("Response was not ok");
        }).then((res) => {
            console.log(res.text());
        }).catch((error) => {
            console.log("There was a problem fetching your information: ", error.message);
        });
    });

});
