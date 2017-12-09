basketService.$inject = ["$http"];

export default basketService;

const ControlURL = "/cart-control/";

function getCookie(c_name) {
    if (document.cookie.length === 0) return "";

    let c_start = document.cookie.indexOf(c_name + "=");
    if (c_start === -1) return "";

    c_start = c_start + c_name.length + 1;
    let c_end = document.cookie.indexOf(";", c_start);
    if (c_end === -1) c_end = document.cookie.length;
    return unescape(document.cookie.substring(c_start, c_end));
}

function basketService($http) {
    this.add = add;
    this.remove = remove;
    this.close = close;
    this.count = count;
    this.load_basket = load_basket;
    const HEADERS = {headers: {'X-CSRFToken': getCookie('csrftoken')}};

    function count (data) {
        return $http.get(ControlURL, Object.assign(HEADERS, {data: data || {}})).then((response) => {
           return response;
        }).catch(console.log);
    }
    function add(data) {
        return $http.post(ControlURL, data, HEADERS).then((response) => {
           return response;
        }).catch(console.log);
    }
    function remove(data) {
        return $http.delete(ControlURL, Object.assign(HEADERS, {data: data || {}})).then((response) => {
           return response;
        }).catch(console.log);
    }

    function close(data) {
        return $http.post("/basket/close/", data, HEADERS).then((response) => {
            return response;
        }).catch(console.log);
    }

    function load_basket() {
        return $http.post("/basket/", {}, HEADERS).then((response) => {
            return response;
        }).catch(console.log);
    }

}