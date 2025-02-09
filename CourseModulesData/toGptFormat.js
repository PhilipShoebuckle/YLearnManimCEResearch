"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var fs = require("fs");
function createBlock(system, user, assistant) {
    return { messages: [{ role: "system", content: system }, { role: "user", content: user }, { role: "assistant", content: assistant }] };
}
var text = require('./khan-academy-units-main/data/2nd_grade_units_subtopics.json');
var system_prompt = "You are an educator who designs course modules";
var jsonl = "";
for (var _i = 0, text_1 = text; _i < text_1.length; _i++) {
    var block = text_1[_i];
    var conversation = createBlock(system_prompt, block.Unit, block.Subtopics);
    jsonl = jsonl + JSON.stringify(conversation) + "\n";
}
var path = './oneJson.jsonl';
fs.writeFileSync(path, jsonl, 'utf8');
