import angular from "angular";

import landing from "./landing.module/landing.module";

const name = "app";

angular
    .module(name, [
        landing
    ]);