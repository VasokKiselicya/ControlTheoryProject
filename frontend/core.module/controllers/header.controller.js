HeaderController.$inject = ["$scope", "$timeout"];

export default HeaderController;

function HeaderController($scope, $timeout) {
    const vm = this;

    vm.language = '';
    vm.hide_choose = true;

    vm.changeLang = (code) => {
        vm.language = code;
        $timeout(() =>  $(document.forms.langForm).submit());
    };

    vm.showChoose = () => {
        vm.hide_choose = !vm.hide_choose;
    };
}