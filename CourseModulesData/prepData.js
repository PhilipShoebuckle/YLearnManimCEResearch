"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var fs = require("fs");
function createBlock(system, user, assistant) {
    return { messages: [{ role: "system", content: system }, { role: "user", content: user }, { role: "assistant", content: assistant }] };
}
var system_prompt = "You are a system that generates course subtopics for a topic prompted";
var jsonDir = fs.readdirSync('./khan-academy-units-main/data');
var jsonl = "";
jsonDir.forEach(function (file) {
    var text = require('./khan-academy-units-main/data/' + file);
    for (var _i = 0, text_1 = text; _i < text_1.length; _i++) {
        var block = text_1[_i];
        var conversation = createBlock(system_prompt, block.Unit, block.Subtopics.splice(1).reduce(function (acc, e) { return acc + "\n" + e; }, block.Subtopics[0]));
        jsonl = jsonl + JSON.stringify(conversation) + "\n";
    }
});
var path = './training_data.jsonl';
fs.writeFileSync(path, jsonl, 'utf8');
