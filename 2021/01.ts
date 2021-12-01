import { readFileSync } from 'fs';

const m = readFileSync('./01input', 'utf-8').split(/\r?\n/).map(Number);
//const m = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

var p1 = 0;
for (var i = 0; i < m.length; i++) {
    if (m[i] < m[i+1]) {
        p1++;
    }
}

var p2 = 0;
for (var i = 0; i < m.length-2; i++) {
    var a = m[i] + m[i+1] + m[i+2];
    var b = m[i+1] + m[i+2] + m[i+3];
    if (a < b) {
        p2++;
    }
}

console.log(p1, p2);
