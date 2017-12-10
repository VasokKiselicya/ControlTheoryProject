scrollArrowDirective.$inject = [];

export default scrollArrowDirective;

function scrollArrowDirective() {
    return {
        restrict: "A",
        link: function (scope, $elm) {
            $elm.on('click', function () {
                $("html, body").animate({scrollTop: $elm.offset().top - 80}, "slow");
            });
        }
    }
}