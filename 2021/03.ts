import { readFileSync } from 'fs';

const diagnostic = readFileSync("./03input").toString().split("\r\n");

var gamma_rate = "";
var epsilon_rate = "";
var turned = [];

for (var i = 0; i < diagnostic[0].length; i++) {
    turned[i] = "";
    for (var d of diagnostic) {
        turned[i] += d[i];
    }
}

for (var c of turned) {
    var count1 = (c.match(/1/g)||[]).length;
    var count0 = (c.match(/0/g)||[]).length;
    if (count1 > count0) {
        gamma_rate += "1";
        epsilon_rate += "0";
    } else {
        gamma_rate += "0";
        epsilon_rate += "1";
    }
}

const power_consumption = parseInt(gamma_rate,2) * parseInt(epsilon_rate,2)
console.log("part1", power_consumption);

var oxygen_candidates = Object.assign([], diagnostic);
var co2_candidates = Object.assign([], diagnostic);
//console.log("oxy candidates start", oxygen_candidates);
//console.log("co2 candidates start", co2_candidates);

for (var i = 0; i <= diagnostic[0].length; i++) {
    //console.log("index", i);
    count1 = 0;
    count0 = 0;
    for (var can of oxygen_candidates) {
        if (can[i] == "1"){
            count1++;
        } else {
            count0++;
        }
    }
    //console.log("1 count =", count1, "; 0 count =", count0)
    for (var j = oxygen_candidates.length-1; j >=0; j--) {
        if (count1 >= count0) {
            if (oxygen_candidates[j][i] == "0"){
                //console.log("remove", oxygen_candidates[j]);
                oxygen_candidates.splice(j, 1);
            }
        } else {
            if (oxygen_candidates[j][i] == "1"){
                //console.log("remove", oxygen_candidates[j]);
                oxygen_candidates.splice(j, 1);
            }
        }
    }
    if (oxygen_candidates.length == 1) {
        break;
    }
}

//console.log("oxy candidates 1", oxygen_candidates.length);
//console.log("co2 candidates 1", co2_candidates.length);

for (var i = 0; i <= diagnostic[0].length; i++) {
    //console.log("index", i);
    count1 = 0;
    count0 = 0;
    for (var can of co2_candidates) {
        if (can[i] == "1"){
            count1++;
        } else {
            count0++;
        }
    }
    //console.log("1 count =", count1, "; 0 count =", count0)
    for (var j = co2_candidates.length-1; j >=0; j--) {
        if (count1 >= count0) {
            if (co2_candidates[j][i] == "1"){
                //console.log("remove", co2_candidates[j]);
                co2_candidates.splice(j, 1);
            }
        } else {
            if (co2_candidates[j][i] == "0"){
                //console.log("remove", co2_candidates[j]);
                co2_candidates.splice(j, 1);
            }
        }
    }
    if (co2_candidates.length == 1) {
        break;
    }
}

//console.log("oxy candidates end", oxygen_candidates.length);
//console.log("co2 candidates end", co2_candidates.length);

const oxygen_generator_rating = parseInt(oxygen_candidates[0],2);
const co2_scrubber_rating = parseInt(co2_candidates[0],2);
const p2 = oxygen_generator_rating * co2_scrubber_rating;
console.log("part2", p2);
