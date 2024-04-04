function applyFrenchRules(word) {
    if (["ffy", "fy", "tiond", "tiont"].some((elem) => word.includes(elem)))
        return null;
    return word.replace("èff", "eff");
}

function cartesianProduct(...arrays) {
    // Voir https://fr.wikipedia.org/wiki/Produit_cart%C3%A9sien
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

function displayResults(combinations) {
    ans = `<p>Nombre de combinaisons : ${combinations.length}</p>`;
    ans += "<ol>";
    combinations.forEach((combination, id) => {
        ans += `<li id="k_${id}">${combination}</li>`;
    });
    ans += "</ol>";
    const resultsDiv = document.getElementById("results");
    resultsDiv.innerHTML = ans;
}

function kreficioner() {
    const phonemes = document
        .getElementById("phonemes")
        .value.split(";")
        .map((group) => group.split(","));
    const combinations = generateCombinations(phonemes);
    displayResults(combinations);
}
