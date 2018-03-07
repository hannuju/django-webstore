$(document).ready(function() {

    // Clicking table row opens item detail view page
    $(".clickable-cell").click(function() {
        window.location = $(this).data("href");
    });

    // AJAX call for adding item to cart
    $('.add-to-cart-button').click(function() {
        let id = $(this).attr("value");
        fetch("/store/item/" + id + "/add_to_cart", {
            credentials: "same-origin"
        })
        .then((response) => {
            if(response.ok) {
                return response;
            }
            throw new Error("Response was not ok");
        }).then((res) => {
            $('.cart').attr('data-content', 'Item added to cart');
            $('.cart').popover('toggle');
            popperHide();
        }).catch((error) => {
            console.log("There was a problem fetching your information: ", error.message);
        });
    });

    // Hides popper in 1,5 seconds
    function popperHide() {
        setTimeout(function() {
            $('.cart').popover('hide');
        }, 1500);
    }

});
