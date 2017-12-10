phoneNumberDirective.$inject = ["$filter", "$browser"];

export default phoneNumberDirective;

function phoneNumberDirective($filter, $browser) {
    return {
        require: 'ngModel',
        restrict: "A",
        link: function (scope, $elm, $attrs, ngModelCtrl) {
            let listener = function() {
                let value = $elm.val().replace(/[^0-9]/g, '');
                $elm.val($filter('tel')(value, false));
            };

            ngModelCtrl.$parsers.push(function(viewValue) {
                return viewValue.replace(/[^0-9]/g, '').slice(0,10);
            });

            ngModelCtrl.$render = function() {
                $elm.val($filter('tel')(ngModelCtrl.$viewValue, false));
            };

            $elm.bind('change', listener);
            $elm.bind('keydown', function(event) {
                let key = event.keyCode;
                if (key === 91 || (15 < key && key < 19) || (37 <= key && key <= 40)){
                    return;
                }
                $browser.defer(listener);
            });

            $elm.bind('paste cut', function() {
                $browser.defer(listener);
            });

        }
    }
}