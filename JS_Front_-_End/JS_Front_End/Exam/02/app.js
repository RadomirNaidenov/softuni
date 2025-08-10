function solve() {
    const typeInput = document.getElementById("type");
    const ageInput = document.getElementById("age");
    const genderSelect = document.getElementById("gender");
    const registerBtn = document.getElementById("register-btn");

    const registeredList = document.getElementById("registered-list");
    const confirmedList = document.getElementById("confirmed-list");

    registerBtn.addEventListener("click", function(e) {
        e.preventDefault();
        const bloodType = typeInput.value.trim();
        const age = ageInput.value.trim();
        const gender = genderSelect.value.trim();

        if (bloodType === "" || age === "" || gender === "") {
            return;
        }

        const li = document.createElement("li");
        const article = document.createElement("article");

        const pType = document.createElement("p");
        pType.textContent = `Blood Type: ${bloodType}`;
        const pAge = document.createElement("p");
        pAge.textContent = `Age: ${age}`;
        const pGender = document.createElement("p");
        pGender.textContent = `Gender: ${gender}`;

        article.appendChild(pType);
        article.appendChild(pAge);
        article.appendChild(pGender);

        const buttonsDiv = document.createElement("div");
        buttonsDiv.className = "buttons";

        const editBtn = document.createElement("button");
        editBtn.className = "edit-btn";
        editBtn.textContent = "Edit";

        const confirmBtn = document.createElement("button");
        confirmBtn.className = "confirm-btn";
        confirmBtn.textContent = "Confirm";

        editBtn.addEventListener("click", function() {
            typeInput.value = bloodType;
            ageInput.value = age;
            genderSelect.value = gender;
            li.remove();
        });

        confirmBtn.addEventListener("click", function() {
            li.remove();
            buttonsDiv.innerHTML = "";
            const clearBtn = document.createElement("button");
            clearBtn.className = "clear-btn";
            clearBtn.textContent = "Clear";
            clearBtn.addEventListener("click", function() {
                li.remove();
            });
            buttonsDiv.appendChild(clearBtn);
            li.appendChild(buttonsDiv);
            confirmedList.appendChild(li);
        });

        buttonsDiv.appendChild(editBtn);
        buttonsDiv.appendChild(confirmBtn);
        li.appendChild(article);
        li.appendChild(buttonsDiv);
        registeredList.appendChild(li);

        typeInput.value = "";
        ageInput.value = "";
        genderSelect.value = "";
    });
}