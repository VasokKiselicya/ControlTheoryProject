scrollArrowDirective.$inject = [];

export default scrollArrowDirective;

function scrollArrowDirective() {
    return {
        restrict: "A",
        link: function (scope, $elm) {
            $elm.on('click', function () {
                console.log($elm.offset());
                $("html, body").animate({scrollTop: $elm.offset().top - 50}, "slow");
            });
        }
    }
}