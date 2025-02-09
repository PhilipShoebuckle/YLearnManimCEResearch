import * as fs from "fs";

interface training_block {
    messages: [{role: "system", content: string}, {role: "user", content: string}, {role: "assistant", content: string}];
}

function createBlock(system: string, user: string, assistant: string): training_block {
    return {messages: [{role: "system", content: system}, {role: "user", content: user}, {role: "assistant", content: assistant}]};
}



// const test = require('./khan-academy-units-main/data/2nd_grade_units_subtopics.json');
// console.log(typeof test[0].Unit);

// const urmom: training_block = createBlock("ur a programmer", "code sorting algorithm in python", "here is the code...");
// const urmom2: training_block = createBlock("ur a programmer", "code sorting algorithm in js", "here is the code...");
// // console.log(urmom);
// // console.log(JSON.stringify(urmom));
// const path = './test.jsonl';
// let a = JSON.stringify(urmom) + "\n" + JSON.stringify(urmom2);
// fs.writeFileSync(path, a, 'utf8');