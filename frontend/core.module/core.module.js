import angular from "angular";

import HeaderController from "./controllers/header.controller";

import scrollArrowDirective from './directives/scroll.directive'

const name = "app.core";

angular
    .module(name, [])

    .directive('scrollArrow', scrollArrowDirective)

    .controller("HeaderController", HeaderController);

export default name;