const express = require("express");
const app = express();
const { spawn } = require("child_process");

app.use(express.json());

function runPythonScript(text, language) {
  const pythonProcess = spawn("python", ["./utils/main.py", text, language]);

  pythonProcess.stdout.on("data", (data) => {
    console.log(`stdout: ${data.toString()}`);
  });

  pythonProcess.stderr.on("data", (data) => {
    console.log(`stderr: ${data.toString()}`);
  });

  pythonProcess.on("exit", (code) => {
    console.log(`Python script exited with code ${code}`);
  });
}

app.post("/translate", (req, res) => {
  const { text, language } = req.body;
  runPythonScript(text, language);
  res.send("Translation and speech conversion in progress.");
});



app.get("/", (req, res) => {
  res.send("Hey, I am Parth, and I am a full stack web developer!");
});

app.listen(3000, () => {
  console.log("Server is running at http://localhost:3000");
});
