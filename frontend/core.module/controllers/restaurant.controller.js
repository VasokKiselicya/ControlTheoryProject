restaurantController.$inject = ["$rootScope", "$scope", "$window"];

export default restaurantController;

function restaurantController($rootScope, $scope, $window) {
    const vm = this;
    vm.slides = [];
    vm.minDate = moment().add(1, "h").startOf("hour");
    vm.maxDate = moment().add(2, "M").endOf("date");

    vm.formValues = {
        fullName: "",
        quantity: 2,
        phone: "0",
        date_time: angular.copy(vm.minDate),
        wishes: ""
    };


    vm.set_items = () => {
        vm.slides = $window.CarouselItems;
    };

}