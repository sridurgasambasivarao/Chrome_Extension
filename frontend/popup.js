document.getElementById("askBtn").addEventListener("click", async () => {
    const question = document.getElementById("question").value;
    const status = document.getElementById("status");
    const answer = document.getElementById("answer");

    answer.innerText = "";
    status.innerText = "Loading...";

    let [tab] = await chrome.tabs.query({
        active: true,
        currentWindow: true
    });

    const currentUrl = tab.url;
    
    try
    {
        const response = await fetch("http://127.0.0.1:8000/ask", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                url: currentUrl,
                question: question
            })
        });

    
        const data = await response.json();

        status.innerText = "";
        answer.innerText = data.answer;
    
    }catch (error) {

        status.innerText = "";
        answer.innerText = "Error retrieving answer.";

    }
});