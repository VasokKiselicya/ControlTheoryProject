LandingController.$inject = ["$rootScope", "$scope"];

export default LandingController;

function LandingController($rootScope, $scope) {
    const vm = this;

    $scope.button_click = (ev) => {
        console.log("HELLO WORLD");
        console.log(ev);
    }

}