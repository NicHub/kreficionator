function applyFrenchRules(word) {
    if (["ffy", "fy", "tiond", "tiont"].some((elem) => word.includes(elem))) {
        word = null;
    } else {
        word = word.replace("èff", "eff");
    }
    return word;
}

function cartesianProduct(...arrays) {
    return arrays.reduce(
        (accumulator, currentArray) => {
            return accumulator.flatMap((item) => {
                return currentArray.map((currentItem) => {
                    return [...item, currentItem.replace("\n", "")];
                });
            });
        },
        [[]]
    );
}

function generateCombinations(phonemes) {
    const combinations = cartesianProduct(...phonemes);
    const filteredCombinations = combinations
        .map((line) => line.join(""))
        .map((line) => applyFrenchRules(line))
        .filter((elem) => elem !== null);
    return filteredCombinations;
}

function displayResults(combinations, phonemes) {
    const resultsDiv = document.getElementById("results");
    ans = "<ol>";
    combinations.forEach((combination, id) => {
        ans += `<li id="k_${id}">${combination}</li>`;
    });
    ans += "</ol>";

    const count = (_l) => {
        if (_l.length === 1) {
            return _l[0];
        } else {
            return _l[0] * count(_l.slice(1));
        }
    };
    ans =
    `<p>Nombre de combinaisons avant application des règles de français: ${count(
        phonemes.map((row) => row.length)
        )}</p>` +
        `<p>Nombre de combinaisons après application des règles de français: ${combinations.length}</p>` +
        ans;
    resultsDiv.innerHTML = ans;
}

function main() {
    const phonemesInput = document.getElementById("phonemes");
    const phonemesValue = phonemesInput.value;
    const phonemes = phonemesValue.split(";").map((group) => group.split(","));
    const combinations = generateCombinations(phonemes);
    displayResults(combinations, phonemes);
}
