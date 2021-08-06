$('.plus-cart').click(function () {
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2]
    $.ajax({
        type: "GET",
        url: "/increase_cart",
        data: { prod_id: id },

        success: function (data) {
            eml.innerText = data.quantity
            document.getElementById("amount").innerText = data.amount
            document.getElementById("total").innerText = data.total
        }
    })
})

$('.minus-cart').click(function () {
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2]
    $.ajax({
        type: "GET",
        url: "/decrease_cart",
        data: { prod_id: id },

        success: function (data) {
            eml.innerText = data.quantity
            document.getElementById("amount").innerText = data.amount
            document.getElementById("total").innerText = data.total
        }
    })
})

$('.remove-cart').click(function () {
    var id = $(this).attr("pid").toString();
    var eml = this
    console.log(id)
    $.ajax({
        type: "GET",
        url: "/remove_cart",
        data: { prod_id: id },

        success: function (data) {
            console.log("Delete")
            document.getElementById("amount").innerText = data.amount
            document.getElementById("total").innerText = data.total
            eml.parentNode.parentNode.parentNode.parentNode.remove()
        }
    })
})


