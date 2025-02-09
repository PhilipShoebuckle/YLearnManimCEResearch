import * as fs from "fs";

interface training_block {
    messages: [{role: "system", content: string}, {role: "user", content: string}, {role: "assistant", content: string}];
}

function createBlock(system: string, user: string, assistant: string): training_block {
    return {messages: [{role: "system", content: system}, {role: "user", content: user}, {role: "assistant", content: assistant}]};
}

const system_prompt = "You are a system that generates course subtopics for a topic prompted"
const jsonDir = fs.readdirSync('./khan-academy-units-main/data');
let jsonl = "";

jsonDir.forEach(file => {

    const text = require('./khan-academy-units-main/data/' + file);

    for (const block of text) { 
        const conversation = createBlock(system_prompt, block.Unit, block.Subtopics.splice(1).reduce((acc, e) => {return acc + "\n" + e;}, block.Subtopics[0]));
        if (conversation.messages[2].content )
        jsonl = jsonl + JSON.stringify(conversation) + "\n";
    }
});

const path = './training_data.jsonl';
fs.writeFileSync(path, jsonl, 'utf8');