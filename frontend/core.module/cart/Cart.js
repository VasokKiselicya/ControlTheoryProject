export default {Cart, Item};

class Cart {
    constructor() {
        this.items = [];
    }

    setItems(items) {
        this.items = items;
    }
    addItem(id, name, q) {
        let find_item;
        this.items.some(item => {
            if (item.getId() === id) return find_item = item;
        });
        if(find_item) {}
        this.items.push(item);
    }

    removeItem(id) {
        this.items.some((item, index) => {
            if (item.getId() === id) return this.items.splice(index, 1);
        });
    }

    isEmpty() {
         return this.items.length === 0;
    }

    _clear() {
        this.items = [];
    }

}

class Item {
    constructor(id, name, quantity) {
        this.id = id;
        this.name = name;
        this.q = quantity;
    }

    getId() {
        return this.id;
    }

    setQuantity(qty) {
        this.q = qty;
    }

}