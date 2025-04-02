const recordButton = document.getElementById("recordButton");
const visualizer = document.querySelector('.visualizer');
let animateWaves = false; 
const bufferLength = 128;
let elements = [];

// Create visualizer elements
for (let i = 0; i < bufferLength; i++) {
    const element = document.createElement('span');
    element.classList.add('element');
    elements.push(element);
    visualizer.appendChild(element);
}

recordButton.addEventListener("click", async function () {
    console.log("Record button clicked");
    animateWaves = true;
    recordButton.style.backgroundColor = "rgb(99, 0, 0)"; 

    try {
        const response = await fetch("http://127.0.0.1:8000/process_speech/", { method: "POST" });
        const data = await response.json();

        var extractedText = data.recognized_text.split(": ")[1];
        console.log("Gemma responce:",extractedText);

        // Display Gemini response
        const geminiResponseElement = document.getElementById("geminiResponse");
        geminiResponseElement.textContent = data.gemini_response;

    } 
    catch (error) {
        console.error("Error:", error);
    }
    // at the end
    animateWaves = false;
    recordButton.style.backgroundColor = "rgb(150, 0, 0)";
});

// Animation loop for the animation
let angleOffset = 0;
const update = () => {
    requestAnimationFrame(update);

    if (animateWaves) {  
        angleOffset += 0.05;

        elements.forEach((element, i) => {
            element.style.opacity = "1";

            let scale = 0.6 + Math.sin(Date.now() / 500 + i * 0.3) * 0.5;
            let distance = 90 + Math.sin(Date.now() / 400 + i * 0.2) * 50;
            let angle = i * (-360 / bufferLength) + angleOffset;

            element.style.transform = `rotateZ(${angle}deg)
                translate(-50%, ${distance}px)
                scale(${scale})`;
        });
    } else {
        elements.forEach(element => {
            element.style.opacity = "0"; 
        });
    }
};

update();
