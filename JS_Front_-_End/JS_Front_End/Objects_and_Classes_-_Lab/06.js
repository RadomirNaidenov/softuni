function manageMeeting(arrayOfStrings) {
    let successfulMeetings = {}


    for (const text of arrayOfStrings) {
        let splitedText = text.split(" ");
        let day = splitedText[0];
        let name = splitedText[1];

        if (!(day in successfulMeetings)) {
            successfulMeetings[day] = name;
            console.log(`Scheduled for ${day}`);
            
        } else {
            console.log(`Conflict on ${day}!`); 
        }
    }

    Object.entries(successfulMeetings).forEach(([key, value]) => {
        console.log(`${key} -> ${value}`);
    })
}

