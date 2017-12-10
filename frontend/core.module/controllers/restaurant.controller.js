restaurantController.$inject = ["$rootScope", "$scope", "$window"];

export default restaurantController;

function restaurantController($rootScope, $scope, $window) {
    const vm = this;
    vm.slides = [];

    vm.set_items = () => {
        vm.slides = $window.CarouselItems;
    }

}