basketService.$inject = ["$http"];

export default basketService;

const ControlURL = "/cart-control/";

function basketService($http) {
    this.add = add;
    this.remove = remove;
    this.close = close;

    function add(data) {
        return $http.post(ControlURL, data).then((response) => {
           return response;
        });
    }
    function remove(data) {
        return $http.delete(ControlURL, data).then((response) => {
           return response;
        });
    }
    function close() {
        return $http.patch(ControlURL, data).then((response) => {
            return response;
        });
    }

}