function validatePaswword(pass) {

    if (!checkLength(pass)) {
        console.log(`Password must be between 6 and 10 characters`);
    }

    if (!checkIsAlphaNumeric(pass)) {
        console.log(`Password must consist only of letters and digits`);
    }

    if (!checkIfExistTwoDigits(pass)) {
        console.log(`Password must have at least 2 digits`);
    }

    if (checkLength(pass) && checkIsAlphaNumeric(pass) && checkIfExistTwoDigits(pass)) {
        console.log(`Password is valid`);
    }

    function checkLength(pass) {
        if (pass.length < 6 || pass.length > 10) {
            return false
        } 

        return true
    }

    function checkIsAlphaNumeric(pass) {
        return /^[A-Za-z0-9]+$/.test(pass);
    }

    function checkIfExistTwoDigits(pass) {
        return /\d.*\d/.test(pass)
    }
}

