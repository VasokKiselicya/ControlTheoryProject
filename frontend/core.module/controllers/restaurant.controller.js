restaurantController.$inject = ["BasketService", "$window"];

export default restaurantController;

function restaurantController(BasketService, $window) {
    const vm = this;
    vm.slides = [];
    vm.minDate = moment().add(1, "h").startOf("hour");
    vm.maxDate = moment().add(2, "M").endOf("date");

    vm.formValues = {
        fullName: "",
        quantity: "",
        phone: "",
        date_time: angular.copy(vm.minDate),
        wishes: ""
    };

    vm.closeBooking = false;

    vm.set_items = () => {
        vm.slides = $window.CarouselItems;
    };

    vm.saveBooking = () => {
        let data = angular.copy(vm.formValues);
        data.date_time = moment.parseZone(data.date_time).format('YYYY-MM-DD HH:mm');
        BasketService
            .booking(data)
            .then(r => {
                console.log(r);
                vm.closeBooking = true;
            })
            .catch(console.log);
    }

}