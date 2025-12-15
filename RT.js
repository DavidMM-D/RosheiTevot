// written by chatGPT and Gemini -- Must be checked and edited!
// Get the output element once at the top for efficiency
const outputElement = document.getElementById("output");

// Replace final Hebrew letters with non-final equivalents
function unfinal(name) {
    const fin = 'ךםןףץ';
    const nor = 'כמנפצ';
    let out = name.split("");

    for (let i = 0; i < out.length; i++) {
        const j = fin.indexOf(out[i]);
        if (j !== -1) {
            out[i] = nor[j];
        }
    }

    return out.join("");
}

// Search for Roshei Tevot matches
function RT(name, allRT, word) {
    const results = [];
    let start = 0;
    const nm = unfinal(name);
    // Start building the HTML output string
    let htmlOutput = ''; 

    while (true) {
        const i = allRT.indexOf(nm, start);
        if (i === -1) break;
        results.push(i);
        start = i + 1;
    }

    // Add summary information to the output
    htmlOutput += `<h3>Results for: ${name}</h3>`;
    // If no matches, display a message
    if (results.length === 0) {
        htmlOutput += `<p>No Roshei Tevot matches found.</p>`;
    } else {
        htmlOutput += `<p>Total matches found: ${results.length}</p>`;
        // Create an unordered list for the matches
        htmlOutput += `<ul>`; 
        for (const e of results) {
            // Add each match as a list item, labeling book, chapter, and verse
            htmlOutput += `<li>${word[e][1]} ${word[e][2]}, ${word[e][3]}: `;
            for (let i = 0; i < name.length; i++) {
                // Highlight the first letter of each word to emphasize the match
                // The rest of the word is added in a lighter color (via a <span>)
                const wordText = word[e + i][0];
                htmlOutput += `<span style="font-weight:bold;">${wordText[0]}</span>`;
                htmlOutput += `<span>${wordText.substring(1)}</span>&nbsp;`;
            }
            htmlOutput += `</li>`;
        }
        htmlOutput += `</ul>`;
    }
    
    // Set the innerHTML of the output element once, clearing any previous results
    outputElement.innerHTML = htmlOutput; 
    
    // You can keep the console logging if you want it for debugging, 
    // but it is no longer required for display.
    // console.log("name entered:", name);
    // console.log("number of matches:", results.length);
}

async function loadData() {
    const word = await fetch("word_bk_ch_v.json").then(r => r.json());
    const allRT = await fetch("allRT.txt").then(r => r.text());
    return { word, allRT };
}

(async () => {
    // Check if the output element was found before proceeding
    if (!outputElement) {
        console.error("Could not find the 'output' element in the HTML.");
        return;
    }
    
    // Initial message while loading
    outputElement.innerHTML = "<p>Loading Torah data... Please wait.</p>";
    
    const { word, allRT } = await loadData();
    
    // Update message after loading
    outputElement.innerHTML = "<p>Data loaded! Enter a name and click OK.</p>";

    document.getElementById("go").onclick = () => {
        const name = document.getElementById("input").value.trim();
        if (!name) return;
        
        // Clear previous results immediately upon clicking
        outputElement.innerHTML = "<p>Searching...</p>"; 
        
        RT(name, allRT, word);
    };
})();