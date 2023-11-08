const questions = [
    {
        question: "Qual é a forma geral de uma função afim?",
        choices: ["y = ax^2 + b", "y = ax + b", "y = x^2 + a", "y = x - b"],
        correct: 1,
        feedback: "Correto! Uma função afim tem a forma y = ax + b."
    },
    {
        question: "O que é necessário para que uma função afim seja crescente?",
        choices: ["O coeficiente angular (a) deve ser positivo.", "O coeficiente angular (a) deve ser negativo.", "O coeficiente linear (b) deve ser positivo.", "O coeficiente linear (b) deve ser negativo."],
        correct: 0,
        feedback: "Correto! Para que uma função afim seja crescente, o coeficiente angular (a) deve ser positivo."
    },
    // Adicione mais perguntas aqui
];

let currentQuestion = 0;
let score = 0;

function showQuestion() {
    const questionElement = document.getElementById("question");
    const choicesElements = document.querySelectorAll("#choices button");

    questionElement.textContent = questions[currentQuestion].question;

    for (let i = 0; i < 4; i++) {
        choicesElements[i].textContent = questions[currentQuestion].choices[i];
    }
}

function checkAnswer(choice) {
    const feedbackElement = document.getElementById("feedback");

    if (choice === questions[currentQuestion].correct) {
        feedbackElement.textContent = questions[currentQuestion].feedback;
        score++;
    } else {
        feedbackElement.textContent = "Incorreto. Tente novamente.";
    }

    feedbackElement.style.display = "block";
    document.getElementById("nextButton").style.display = "block";

    for (let i = 0; i < 4; i++) {
        document.getElementById("choice" + i).disabled = true;
    }
}

function nextQuestion() {
    if (currentQuestion < questions.length - 1) {
        currentQuestion++;
        showQuestion();
        resetQuestion();
    } else {
        showResults();
    }
}

function resetQuestion() {
    const feedbackElement = document.getElementById("feedback");
    const nextButton = document.getElementById("nextButton");

    feedbackElement.style.display = "none";
    nextButton.style.display = "none";

    for (let i = 0; i < 4; i++) {
        document.getElementById("choice" + i).disabled = false;
    }
}

function showQuestion() {
    const questionElement = document.getElementById("question");
    const choicesElements = document.querySelectorAll("#choices label");

    questionElement.textContent = questions[currentQuestion].question;

    for (let i = 0; i < 4; i++) {
        choicesElements[i].textContent = questions[currentQuestion].choices[i];
    }

    // Limpando as seleções de respostas anteriores
    const radioButtons = document.querySelectorAll('input[type="radio"]');
    for (let i = 0; i < radioButtons.length; i++) {
        radioButtons[i].checked = false;
    }
}

function checkAnswer() {
    const feedbackElement = document.getElementById("feedback");

    const selectedAnswer = document.querySelector('input[name="answer"]:checked');
    if (selectedAnswer) {
        const choiceIndex = parseInt(selectedAnswer.id.slice(-1));

        if (choiceIndex === questions[currentQuestion].correct) {
            feedbackElement.textContent = questions[currentQuestion].feedback;
            score++;
        } else {
            feedbackElement.textContent = "Incorreto. Tente novamente.";
        }

        feedbackElement.style.display = "block";
        document.getElementById("nextButton").style.display = "block";

        for (let i = 0; i < 4; i++) {
            document.getElementById("choice" + i).disabled = true;
        }
    } else {
        feedbackElement.textContent = "Por favor, selecione uma resposta.";
        feedbackElement.style.display = "block";
    }
}

showQuestion();
