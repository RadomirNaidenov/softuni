function vikingSaga(input) {
    let n = Number(input.shift());
    let warriors = {};

    for (let i = 0; i < n; i++) {
        let [name, weapon, strength] = input.shift().split("-");
        strength = Number(strength);
        warriors[name] = {
            weapons: [weapon],
            strength: strength
        };
    }

    while (true) {
        let commandLine = input.shift();
        if (commandLine === "The Saga Ends") break;

        let parts = commandLine.split(" -> ");
        let action = parts[0];
        let name = parts[1];

        if (!warriors[name] || warriors[name].strength <= 0) {
            continue;
        }

        if (action === "Raid") {
            let weapon = parts[2];
            let required = Number(parts[3]);
            if (warriors[name].weapons.includes(weapon) && warriors[name].strength >= required) {
                warriors[name].strength -= required;
                console.log(`${name} fought bravely with ${weapon} and now has ${warriors[name].strength} strength!`);
            } else {
                console.log(`${name} couldn't join the raid with ${weapon}!`);
            }
        } else if (action === "Train") {
            let gained = Number(parts[2]);
            if (warriors[name].strength >= 100) {
                console.log(`${name} is already at full strength!`);
            } else {
                let actualGained = Math.min(100 - warriors[name].strength, gained);
                warriors[name].strength += actualGained;
                console.log(`${name} trained hard and gained ${actualGained} strength!`);
            }
        } else if (action === "Forge") {
            let newWeapon = parts[2];
            if (warriors[name].weapons.includes(newWeapon)) {
                console.log(`${name} already wields ${newWeapon}.`);
            } else {
                warriors[name].weapons.push(newWeapon);
                console.log(`${name} has forged a new weapon: ${newWeapon}!`);
            }
        }
    }

    for (let name of Object.keys(warriors)) {
        if (warriors[name].strength > 0) {
            console.log(`Warrior: ${name}`);
            console.log(`- Weapons: ${warriors[name].weapons.join(", ")}`);
            console.log(`- Strength: ${warriors[name].strength}`);
        }
    }
}