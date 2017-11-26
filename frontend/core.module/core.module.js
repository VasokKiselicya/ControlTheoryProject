import angular from "angular";

import HeaderController from "./controllers/header.controller";

import scrollArrowDirective from './directives/scroll.directive'
import hoveredImageDirective from './directives/hovered-image.directive'

import basketService from "./services/basket.service";

const name = "app.core";

angular
    .module(name, [])

    .directive('scrollArrow', scrollArrowDirective)
    .directive('hoveredImage', hoveredImageDirective)

    .service("BasketService", basketService)

    .controller("HeaderController", HeaderController);

export default name;