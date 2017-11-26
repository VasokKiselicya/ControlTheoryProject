import angular from "angular";

import HeaderController from "./controllers/header.controller";
import BasketController from "./controllers/basket.controller";

import scrollArrowDirective from './directives/scroll.directive'
import hoveredImageDirective from './directives/hovered-image.directive'

import basketService from "./services/basket.service";

const name = "app.core";

angular
    .module(name, [])

    .directive('scrollArrow', scrollArrowDirective)
    .directive('hoveredImage', hoveredImageDirective)

    .service("BasketService", basketService)

    .controller("BasketController", BasketController)
    .controller("HeaderController", HeaderController);

export default name;