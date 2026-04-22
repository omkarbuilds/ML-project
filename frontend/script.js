async function analyzeResume() {

    console.log("🔥 JS RUNNING");

    let file = document.getElementById("resume").files[0];
    let jd = document.getElementById("jd").value;

    if (!file) {
        alert("Upload resume");
        return;
    }

    if (!jd.trim()) {
        alert("Enter job description");
        return;
    }

    let formData = new FormData();
    formData.append("resume", file);
    formData.append("jd", jd);

    document.getElementById("result").innerHTML = "⏳ Analyzing...";

    try {
        let res = await fetch("http://127.0.0.1:5000/analyze", {
            method: "POST",
            body: formData
        });

        let data = await res.json();

        if (data.error) {
            document.getElementById("result").innerHTML = `❌ ${data.error}`;
            return;
        }

        // 🔥 SMART UI
        document.getElementById("score").innerText = "ATS Score: " + data.score + "%";

        document.getElementById("missing").innerHTML =
            "<b>Missing Skills:</b><br>" +
            (data.missing_skills.length
                ? data.missing_skills.map(s => "• " + s).join("<br>")
                : "None 🎯");

        document.getElementById("suggestions").innerHTML =
            "<b>Suggestions:</b><br>" +
            (data.suggestions.length
                ? data.suggestions.map(s => "• " + s).join("<br>")
                : "Looks good 🚀");

        document.getElementById("result").innerHTML = `
            <h3>📊 Detailed Analysis</h3>
            <p><b>ATS Score:</b> ${data.score}%</p>
            <p><b>Missing Skills:</b><br>${data.missing_skills.join("<br>")}</p>
            <p><b>Suggestions:</b><br>${data.suggestions.join("<br>")}</p>
        `;

    } catch (err) {
        console.error(err);
        document.getElementById("result").innerHTML = "❌ Backend connection error";
    }
}