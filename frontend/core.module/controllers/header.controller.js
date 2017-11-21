HeaderController.$inject = ["$scope", "$timeout", "$window"];

export default HeaderController;

function HeaderController($scope, $timeout, $window) {
    const vm = this;

    vm.language = '';
    vm.base_url = "/";
    vm.hide_choose = true;

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
}