window.onload = function () {

    let _quantity, _price, orderItemNum, deltaQuantity, orderItemQuantity, deltaCost
    let quantityArr = []
    let priceArr = []

    let totalForms = parseInt($('input[name=order_items-TOTAL_FORMS]').val());
    // console.log(totalForms);

    let orderTotalQuantity = parseInt($('.order_total_quantity').text()) || 0;
    let orderTotalPrice = parseInt($('.order_total_cost').text().replace(',', '.')) || 0;


    for (let i = 0; i < totalForms; i++) {
        _quantity = parseInt($('input[name=order_items-' + i + '-quantity]').val());
        _price = parseInt($('.orderitems-' + i + '-price').text().replace(',', '.'));

        quantityArr[i] = _quantity;
        if (_price) {
            priceArr[i] = _price;
        } else {
            priceArr[i] = 0
        }
    }

    // // console.info('PRICE', priceArr)
    // // console.info('QUANTITY', quantityArr)
    //
    // $('.order_form').on('click', 'select[name=' + 'order_items-' + (totalForms - 1).toString() + '-product]', function (){
    //     let target = event.target;
    //     console.log(target.value)
    //
    //     $.ajax({
    //         url: '/orders/add_pro/' + target.value + '/',
    //         success: function (data){
    //             // console.log(data)
    //             // $('.order_form').html(data)
    //             let elem = document.getElementsByClassName('td3')
    //             elem = elem[totalForms]
    //             data = data + ' руб'
    //             $(elem).html(data)
    //         },
    //     });
    //     event.preventDefault()
    // })



    $('.order_form').on('click', 'input[type=number]', function () {
        let target = event.target;
        orderItemNum = parseInt(target.name.replace('order_items-', '').replace('-quantity', ''));
        if (priceArr[orderItemNum]) {
            orderItemQuantity = parseInt(target.value);
            deltaQuantity = orderItemQuantity - quantityArr[orderItemNum];
            quantityArr[orderItemNum] = orderItemQuantity;
            orderSummerUpdate(priceArr[orderItemNum], deltaQuantity)
        }
    })

    $('.order_form').on('click', 'input[type=checkbox]', function (){
        let target = event.target;
        orderItemNum = parseInt(target.name.replace('order_items-', '').replace('-DELETE', ''));
        if (target.checked){
            deltaQuantity = -quantityArr[orderItemNum];
        }else {
            deltaQuantity = quantityArr[orderItemNum];
        }
        orderSummerUpdate(priceArr[orderItemNum], deltaQuantity)
    })

    function orderSummerUpdate(orderItemPrice, deltaQuantity) {
        deltaCost = orderItemPrice * deltaQuantity;
        orderTotalPrice = Number((orderTotalPrice + deltaCost).toFixed(2));
        orderTotalQuantity = orderTotalQuantity + deltaQuantity;

        $('.order_total_quantity').html(orderTotalQuantity.toString());
        $('.order_total_cost').html(orderTotalPrice.toString() + ',00');
    }


    $('.formset_row').formset({
        addText: ' добавить продукт',
        deleteText: ' удалить',
        prefix: 'order_items',
        removed: deleteOrderItem,
    });
    function deleteOrderItem(row){
        let targetName = row[0].querySelector('input[type="number"]').name;
        orderItemNum = parseInt(targetName.replace('order_items-', '').replace('-quantity', ''));
        deltaQuantity = -quantityArr[orderItemNum];
        orderSummerUpdate(priceArr[orderItemNum], deltaQuantity)
    }
}