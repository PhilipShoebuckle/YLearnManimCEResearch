import * as fs from "fs";

interface training_block {
    messages: [{role: "system", content: string}, {role: "user", content: string}, {role: "assistant", content: string}];
}

function createBlock(system: string, user: string, assistant: string): training_block {
    return {messages: [{role: "system", content: system}, {role: "user", content: user}, {role: "assistant", content: assistant}]};
}

const text = require('./khan-academy-units-main/data/2nd_grade_units_subtopics.json');
const system_prompt = "You are an educator who designs course modules"

let jsonl = "";

for (const block of text) {
    const conversation = createBlock(system_prompt, block.Unit, block.Subtopics);
    jsonl = jsonl + JSON.stringify(conversation) + "\n";
}

const path = './oneJson.jsonl';
fs.writeFileSync(path, jsonl, 'utf8');
