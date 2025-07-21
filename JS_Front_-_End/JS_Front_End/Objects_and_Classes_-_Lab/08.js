function sayMeow(array) {
    class Cat {
        constructor(name, age) {
            this.name = name;
            this.age = age;
        }

        meow() {
            console.log(`${this.name}, age ${this.age} says Meow`);
        }
    }

    array.forEach(text => {
        let [name, age] = text.split(" ");
        let cat = new Cat(name, age);
        cat.meow();
    });
}

