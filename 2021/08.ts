import { readFileSync } from 'fs';
import { Set } from "immutable";

const data = readFileSync("./08input").toString().split("\n");

function main() {
    console.log("part1", part1(data));
    console.log("part2", part2(data));
}

function part1(data: string[]): number {
    let result = 0;
    for (let line of data) {
        const [patterns, outputs] = line.split("|");
        const out = outputs.trim().split(" ");
        for (let n of out) {
            if (n.length == 2 || n.length == 3 || n.length == 4 || n.length == 7) {
                result++;
            }
        }
    }
    return result;
}

function part2(data: string[]): number {
    let result = 0;
    for (let line of data) {
        const [patterns, outputs] = line.split("|");
        const patternsSet = patterns.trim().split(" ").map(Set);
        
        let onePattern = patternsSet.find((x) => x.size === 2);
        let sevenPattern = patternsSet.find((x) => x.size === 3);
        let fourPattern = patternsSet.find((x) => x.size === 4);
        let eightPattern = patternsSet.find((x) => x.size === 7);
        // if size == 5 then {2,3,5} pattern
        let threePattern = patternsSet.find((x) => x.size === 5 && x.isSuperset(sevenPattern));
        let fivePattern = patternsSet.find((x) => x.size === 5 && !x.isSuperset(sevenPattern) && x.intersect(fourPattern).size === 3);
        let twoPattern = patternsSet.find((x) => x.size === 5 && !x.isSuperset(sevenPattern) && x.intersect(fourPattern).size !== 3);
        // if size == 6 then {0,6,9} pattern
        let ninePattern = patternsSet.find((x) => x.size === 6 && x.isSuperset(fourPattern));
        let zeroPattern = patternsSet.find((x) => x.size === 6 && !x.isSuperset(fourPattern) && x.isSuperset(sevenPattern));
        let sixPattern = patternsSet.find((x) => x.size === 6 && !x.isSuperset(fourPattern) && !x.isSuperset(sevenPattern));

        let pattern = [
            zeroPattern,
            onePattern,
            twoPattern,
            threePattern,
            fourPattern,
            fivePattern,
            sixPattern,
            sevenPattern,
            eightPattern,
            ninePattern
        ];

        let digits = outputs.trim().split(" ").map(Set).map((p) => pattern.findIndex((p2) => p2.equals(p)));
        //console.log(digits.join(""));
        result += parseInt(digits.join(""));
    }
    return result;
}

main();
