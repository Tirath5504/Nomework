import express from "express"
import cors from "cors"
import textPrompt from "./routes/textprompt.js"
const app = express()
const port = 4000
app.use(express.json())
app.use(cors())

app.use("/textprompt", textPrompt);
app.get("/", (req, res) => {
    res.send("workin")
})


app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`)
})