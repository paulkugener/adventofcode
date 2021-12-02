import { readFileSync } from 'fs';

const route = readFileSync("./02input").toString().split("\r\n").map((x) => x.split(" "));

var position = 0;
var depth = 0;

for (var i of route) {
    var instr = i[0];
    var val = parseInt(i[1]);

    switch (instr) {
        case "forward":
            position += val;
            break;
        case "down":
            depth += val;
            break;
        case "up":
            depth -= val;
            break;
        default:
            console.log("error");
            break;
    }
}

console.log("part 1:", position*depth);

position = 0;
depth = 0;
var aim = 0;

for (var i of route) {
    var instr = i[0];
    var val = parseInt(i[1]);

    switch (instr) {
        case "forward":
            position += val;
            depth += (aim * val);
            break;
        case "down":
            aim += val;
            break;
        case "up":
            aim -= val;
            break;
        default:
            console.log("error");
            break;
    }
}

console.log("part 2:", position*depth);
