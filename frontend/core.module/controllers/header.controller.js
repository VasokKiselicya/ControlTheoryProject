HeaderController.$inject = ["$rootScope", "$scope", "$timeout", "$window", "BasketService"];

export default HeaderController;

function HeaderController($rootScope, $scope, $timeout, $window, BasketService) {
    const vm = this;

    vm.language = '';
    vm.base_url = "/";
    vm.basket_url = "/basket/";
    vm.hide_choose = true;
    $rootScope.basket_len = 0;
    loadCount();

    function loadCount() {
        BasketService.count().then(res=> {
            $rootScope.basket_len = parseInt(res.data.count);
        })
    }

    vm.changeLang = (code) => {
        vm.language = code;
        $timeout(() =>  $(document.forms.langForm).submit());
    };

    vm.logout = () => {
        $(document.forms.logoutForm).submit();
    };

    vm.showChoose = () => {
        vm.hide_choose = !vm.hide_choose;
    };

    vm.toMain = () => {
        $window.location.href = vm.base_url;
    };

    vm.load_basket = () => {
        $window.location.href = vm.basket_url;
    }
}