
const input = [4,2,4,1,5,1,2,2,4,1,1,2,2,2,4,4,1,2,1,1,4,1,2,1,2,2,2,2,5,2,2,3,1,4,4,4,1,2,3,4,4,5,4,3,5,1,2,5,1,1,5,5,1,4,4,5,1,3,1,4,5,5,5,4,1,2,3,4,2,1,2,1,2,2,1,5,5,1,1,1,1,5,2,2,2,4,2,4,2,4,2,1,2,1,2,4,2,4,1,3,5,5,2,4,4,2,2,2,2,3,3,2,1,1,1,1,4,3,2,5,4,3,5,3,1,5,5,2,4,1,1,2,1,3,5,1,5,3,1,3,1,4,5,1,1,3,2,1,1,1,5,2,1,2,4,2,3,3,2,3,5,1,5,1,2,1,5,2,4,1,2,4,4,1,5,1,1,5,2,2,5,5,3,1,2,2,1,1,4,1,5,4,5,5,2,2,1,1,2,5,4,3,2,2,5,4,2,5,4,4,2,3,1,1,1,5,5,4,5,3,2,5,3,4,5,1,4,1,1,3,4,4,1,1,5,1,4,1,2,1,4,1,1,3,1,5,2,5,1,5,2,5,2,5,4,1,1,4,4,2,3,1,5,2,5,1,5,2,1,1,1,2,1,1,1,4,4,5,4,4,1,4,2,2,2,5,3,2,4,4,5,5,1,1,1,1,3,1,2,1];

const test_input = [3,4,3,1,2];

function main() {
    run(input, 80);
    run2(input, 80);
    run2(input, 256);
}

function run(state: number[], days: number): void {
    var result = state;
    var d = 1;
    while (days > 0) {
        result = next_day(result);
        //console.log("after", d++, "days :", result.toString())
        days--;
    }
    console.log("number of fish", result.length);
}

function next_day(state: number[]): number[] {
    var result = [];
    for (var f of state) {
        if (f == 0) {
            result.push(...[6, 8]);
        } else {
            result.push(--f);
        }
    }
    return result;
}

function run2(state: number[], days: number): void {
    var result = transform(state);
    while (days > 0) {
        result = next_day2(result);
        //console.log(result.toString())
        days--;
    }
    console.log("number of fish", result.reduce((sum, current) => sum + current, 0));
}

function transform(state: number[]): number[] {
    var result = Array(9).fill(0);
    for (var f of state) {
        result[f]++;
    }
    return result;
}

function next_day2(state: number[]): number[] {
    var result = Array(9).fill(0);
    result[0] = state[1];
    result[1] = state[2];
    result[2] = state[3];
    result[3] = state[4];
    result[4] = state[5];
    result[5] = state[6];
    result[6] = state[7] + state[0];
    result[7] = state[8];
    result[8] = state[0];
    return result;
}

main();