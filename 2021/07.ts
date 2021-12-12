import { readFileSync } from 'fs';

const input = readFileSync("./07input").toString().trim().split(",").map((x) => parseInt(x));
const part2 = true;

function main() {
    console.log(get_best_hor(input));
}

function get_best_hor(arr: number[]): number {
    const min = Math.min(...arr);
    const max = Math.max(...arr);
    var costs = new Array(max).fill(999999);
    for (var i = min; i < max; i++) {
        costs[i] = get_cost(arr, i);
    }
    return Math.min(...costs);
}

function compute_difference(arr: number[], target: number): number[] {
    var result = [];
    for (var i = 0; i < arr.length; i++) {
        if (part2 == true) {
            result[i] = p2cost(Math.abs(arr[i] - target));
        } else {
            result[i] = Math.abs(arr[i] - target);
        }
    }
    return result;
}

function get_cost(arr: number[], target: number): number {
    const result = compute_difference(arr, target);
    return result.reduce((sum, current) => sum + current, 0);
}

function p2cost(distance: number): number {
    var result = 0;
    var tmp = 0;
    while (tmp <= distance) {
        result += tmp;
        tmp++;
    }
    return result;
}

main();