import angular from "angular";

import landing from "./landing.module/landing.module";
import core from "./core.module/core.module";

const name = "app";

angular
    .module(name, [
        landing,
        core
    ])
    .config(['$interpolateProvider', function ($interpolateProvider) {
        $interpolateProvider.startSymbol('[[');
        $interpolateProvider.endSymbol(']]');
    }]);
