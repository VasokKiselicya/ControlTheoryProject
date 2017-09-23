import angular from "angular";

import LandingController from "./controllers/landing.controller";

const name = "app.landing";

angular
    .module(name, [])

    .controller("LandingController", LandingController)

export default name;