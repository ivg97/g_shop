function add (){
    $('.add-to-cart').on('click', 'a', function (){
        let value = event.target;
        console.log(value.name)

        $.ajax({
            url: '/baskets/add/' + value.name + '/'
        })
        event.preventDefault()
    })
}

add()
