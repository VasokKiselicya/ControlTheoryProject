phoneNumberFilter.$inject = [];

export default phoneNumberFilter;

function phoneNumberFilter() {
    return function (tel) {
        if (!tel) return '';

        let value = tel.toString().trim().replace(/^\+/, '');

        if (value.match(/[^0-9]/)) return tel;

        let city, number;

        if (value.length <= 3) city = value;
        else {
            city = value.slice(0, 3);
            number = value.slice(3);
        }

        if (number) {
            if (number.length > 3) {
                number = number.slice(0, 3) + '-' + number.slice(3, 7);
            }
            return ("(" + city + ") " + number).trim();
        }
        else return "(" + city;

    };
}