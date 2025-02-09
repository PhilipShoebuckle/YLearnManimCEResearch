import * as fs from "fs";

interface training_block {
    messages: [{role: "system", content: string}, {role: "user", content: string}, {role: "assistant", content: string}];
}

function createBlock(system: string, user: string, assistant: string): training_block {
    return {messages: [{role: "system", content: system}, {role: "user", content: user}, {role: "assistant", content: assistant}]};
}

const system_prompt = "You are a python programmer that specializes in writing animation code using the Manim Community Edition library";
const user_prompt = "Write example code depicting: ";
let jsonl = "";

for(let i=0; i < 50; i++) {
    const conversation = createBlock(system_prompt, user_prompt, "");
    jsonl = jsonl + JSON.stringify(conversation) + "\n";
}

const path = './trainingData.jsonl';
fs.writeFileSync(path, jsonl, 'utf8');