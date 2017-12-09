BasketController.$inject = ["$rootScope", "BasketService"];

export default BasketController;

function BasketController($rootScope, BasketService) {
    const vm = this;
    vm.cart_loaded = false;
    vm.cartItems = [];
    vm.totalCost = 0;
    vm.MIN = 1;
    vm.MAX = 20;
    vm.basketIsClosed = false;
    vm.address = "";
    
    function calculateCost() {
        vm.totalCost = vm.cartItems.map(x => +x.price * +x.quantity).reduce((a, b) => a + b, 0);
    }

    vm.addToBasket = (product_id, quantity=1, update=false) => {
        BasketService.add({product_id, quantity, update}).then(res => {
            if (res.status !== 200) return;
            $rootScope.basket_len = res.data.count;
        }).catch(console.log);
    };

    vm.changeBasketItem = (item, step=1) => {
        item.quantity += step;
        if (item.quantity > vm.MAX) item.quantity = vm.MAX;
        else if (item.quantity < vm.MIN) item.quantity = vm.MIN;
        else vm.addToBasket(item.product.id, item.quantity, true);
        item.total_price = +item.quantity * +item.price;
        return calculateCost();
    };

    vm.removeFromBasket = (product_id, idx) => {
        vm.cartItems.splice(idx, 1);
        calculateCost();
        BasketService.remove({product_id}).then(res => {
            if (res.status !== 200) return;
            $rootScope.basket_len = res.data.count;
        }).catch(console.log);
    };

    vm.loadCart = () => {
        BasketService
            .load_basket()
            .then((res) => {
                if (res.status !== 200) return;
                vm.cartItems = res.data.basket;
                calculateCost();
                vm.cart_loaded = true;
            })
            .catch(console.log)
    };

    vm.closeBasket = () => {
        BasketService
            .close({address: vm.address})
            .then(res => {
                if (res.status !== 200) return;
                $rootScope.basket_len = 0;
                vm.basketIsClosed = true;
                vm.cartItems = [];
            })
            .then(() => $(window).scrollTop(0))
            .catch(console.log)
    }

}