function askQuestion() {
  let question = document.getElementById("question").value;

  if (question.trim() === "") {
    alert("Please enter a question");
    return;
  }

  fetch("/ask", {
    method: "POST",

    headers: {
      "Content-Type": "application/json",
    },

    body: JSON.stringify({
      question: question,
    }),
  })
    .then((response) => response.json())

    .then((data) => {
      let messages = document.getElementById("messages");

      messages.innerHTML += `
        <div class="user-message">
            <b>You:</b> ${question}
        </div>

        <div class="bot-message">
            <b>Category:</b> ${data.category}<br>
            <b>Answer:</b> ${data.answer}
        </div>
        `;

      messages.scrollTop = messages.scrollHeight;

      speakAnswer(data.answer);

      document.getElementById("question").value = "";
    })

    .catch((error) => {
      console.log(error);
    });
}

function speakAnswer(text) {
  const speech = new SpeechSynthesisUtterance(text);

  speech.lang = "en-US";

  window.speechSynthesis.speak(speech);
}

function startVoice() {
  if (!("webkitSpeechRecognition" in window)) {
    alert("Speech Recognition not supported");
    return;
  }

  const recognition = new webkitSpeechRecognition();

  recognition.lang = "en-US";

  recognition.onresult = function (event) {
    document.getElementById("question").value = event.results[0][0].transcript;
  };

  recognition.start();
}

function translateText() {
  let text = document.getElementById("translateText").value;

  let language = document.getElementById("language").value;

  fetch("/translate", {
    method: "POST",

    headers: {
      "Content-Type": "application/json",
    },

    body: JSON.stringify({
      text: text,
      language: language,
    }),
  })
    .then((response) => response.json())

    .then((data) => {
      document.getElementById("translatedResult").innerText = data.translated;
    });
}

function generateComplaint() {
  let name = document.getElementById("name").value;

  let issue = document.getElementById("issue").value;

  fetch("/complaint", {
    method: "POST",

    headers: {
      "Content-Type": "application/json",
    },

    body: JSON.stringify({
      name: name,
      issue: issue,
    }),
  })
    .then((response) => response.json())

    .then((data) => {
      document.getElementById("complaintResult").innerText = data.complaint;
    });
}
