"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var fs = require("fs");
function createBlock(system, user, assistant) {
    return { messages: [{ role: "system", content: system }, { role: "user", content: user }, { role: "assistant", content: assistant }] };
}
var system_prompt = "You are a python programmer that specializes in writing animation code using the Manim Community Edition library";
var user_prompt = "Write example code depicting: ";
var jsonl = "";
for (var i = 0; i < 50; i++) {
    var conversation = createBlock(system_prompt, user_prompt, "");
    jsonl = jsonl + JSON.stringify(conversation) + "\n";
}
var path = './trainingData.jsonl';
fs.writeFileSync(path, jsonl, 'utf8');
