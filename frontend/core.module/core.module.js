import angular from "angular";

import HeaderController from "./controllers/header.controller";
import BasketController from "./controllers/basket.controller";
import RestaurantController from "./controllers/restaurant.controller";

import scrollArrowDirective from './directives/scroll.directive';
import hoveredImageDirective from './directives/hovered-image.directive';
import phoneNumberDirective from './directives/phone-number.directive';

import phoneNumberFilter from './directives/phone.filter';

import basketService from "./services/basket.service";

const name = "app.core";

angular
    .module(name, [])

    .filter('tel', phoneNumberFilter)

    .directive('scrollArrow', scrollArrowDirective)
    .directive('hoveredImage', hoveredImageDirective)
    .directive('phoneNumber', phoneNumberDirective)

    .service("BasketService", basketService)

    .controller("RestaurantController", RestaurantController)
    .controller("BasketController", BasketController)
    .controller("HeaderController", HeaderController);

export default name;