hoveredImageDirective.$inject = [];

export default hoveredImageDirective;

function hoveredImageDirective() {
    return {
        restrict: "A",
        link: function (scope, $elm) {
            $elm.on("mouseleave", () => {
                $($($elm.parents()[0]).children()[0]).removeClass("active-hover");
            });
            $elm.on('mouseenter', () => {
                $($($elm.parents()[0]).children()[0]).addClass("active-hover");
            });
        }
    }
}