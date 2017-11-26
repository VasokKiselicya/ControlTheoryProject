BasketController.$inject = ["$rootScope", "$scope", "$timeout", "$window", "BasketService"];

export default BasketController;

function BasketController($rootScope, $scope, $timeout, $window, BasketService) {
    const vm = this;
    vm.cart_loaded = false;
    vm.cartItems = [];

    vm.addToBasket = (product_id, quantity=1) => {
        BasketService.add({product_id, quantity}).then(res => {
            if (res.status !== 200) return;
            $rootScope.basket_len = res.data.count;
        }).catch(console.log);
    };

    vm.removeFromBasket = (product_id, idx) => {
        vm.cartItems.splice(idx, 1);
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
                vm.cart_loaded = true;
                console.log(vm.cartItems);
            })
            .catch(console.log)
    };
}