import express from "express"
const router = express.Router()
import {client} from "../client/dist/index.js"
import esource from 'eventsource';
global.EventSource = esource


router.post("/", async (req, res) => {
    try {
    const data = req.body
    console.log(data)
    const app = await client("https://siddhantuniyal-mumbaihacks-genai.hf.space/--replicas/dncnn");
    const result = await app.predict("/predict", [
        data.level, // string  in 'level' Textbox component		
        data.characters, // string  in 'number_of_words' Textbox component		
        data.mistakes, // string  in 'how_many_errors' Textbox component		
        data.prompt, // string  in 'topic' Textbox component
    ],{
        timeout: 100000,

    });

    const strRes = result.data ;
    const resultStr = strRes.join("");
    res.json({result:resultStr})

} catch (error) {
        console.log(error)
}
})

export default router;