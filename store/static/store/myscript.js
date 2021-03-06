$(document).ready(function() {

    // Clicking table row opens item detail view page
    $(".clickable-cell").click(function() {
        window.location = $(this).data("href");
    });

    // AJAX call for adding item to cart
    // Triggers popover after successful response
    $(".add-to-cart-button").click(function() {
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
            $(".cart").attr('data-content', 'Item added to cart');
            $(".cart").popover("show");
            popperHide();
        }).catch((error) => {
            console.log("There was a problem fetching your information: ", error.message);
        });
    });

    // Initialize popover
    $(function () {
      $("[data-toggle='popover']").popover()
    })

    // Hides popover in 1,5 seconds
    function popperHide() {
        setTimeout(function() {
            $(".cart").popover("hide");
            $(".cart").attr("data-content", "");
        }, 1500);
    }

});
