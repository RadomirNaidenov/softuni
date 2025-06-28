function determinesDriver(driverSpeed, area) {
    let areaLimits =  {
        "motorway": 130,
        "interstate": 90,
        "city": 50,
        "residential": 20
    };

    if (areaLimits[area] >= driverSpeed) {
        console.log(`Driving ${driverSpeed} km/h in a ${areaLimits[area]} zone`);
        
    } else {
        let speedDiff = driverSpeed - areaLimits[area];

        if (speedDiff <= 20) {
            console.log(`The speed is ${speedDiff} km/h faster than the allowed speed of ${areaLimits[area]} - speeding`);
        } else if (speedDiff <= 40) {
            console.log(`The speed is ${speedDiff} km/h faster than the allowed speed of ${areaLimits[area]} - excessive speeding`);
        } else {
            console.log(`The speed is ${speedDiff} km/h faster than the allowed speed of ${areaLimits[area]} - reckless driving`); 
        }
    }
}