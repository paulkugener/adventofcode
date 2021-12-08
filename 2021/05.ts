import { readFileSync } from 'fs';
import { mainModule } from 'process';

const input = readFileSync("./05input").toString().trim().split("\r\n").map((item) => item.trim().split(" -> ").map((e) => e.trim().split(",").map((a) => parseInt(a))));

//x1,y1 -> x2,y2

function main() {
    const part2 = true;
    var map = initMap();
    map = makeLines(map, part2);
    //drawMap(map);
    console.log(intersectionCount(map));
}

function intersectionCount(map: number[][]): number {
    var result = 0;
    for (var line of map) {
        for (var v of line) {
            if (v > 1) result++;
        }
    }
    return result;
}

function makeLines(map: number[][], part2: boolean): number[][] {
    for (var line of input) {
        var x1 = line[0][0];
        var y1 = line[0][1];
        var x2 = line[1][0];
        var y2 = line[1][1];
        if (x1 == x2) {
            // horizontal
            const max = Math.max(y1, y2);
            const min = Math.min(y1, y2);
            for (var i = min; i <= max; i++) {
                map[i][x1] += 1;
            }
        } else if (y1 == y2) {
            //vertical
            const max = Math.max(x1, x2);
            const min = Math.min(x1, x2);
            for (var i = min; i <= max; i++) {
                map[y1][i] += 1;
            }
        } else if (part2) {
            // diagonal
            while (x1 != x2) {
                map[y1][x1] += 1;
                if (x1 < x2) x1++;
                else x1--;
                if (y1 < y2) y1++;
                else y1--;
            }
            map[y2][x2] += 1;
        }
    }
    return map;
}

function drawMap(map: number[][]) {
    for (var line of map) {
        console.dir(line.toString().replace(/\,/gi, ' ').replace(/0/gm, '.'));
    }
}

function initMap(): number[][] {
    var max_x = 0;
    var max_y = 0;
    for (var line of input) {
        var x1 = line[0][0];
        var y1 = line[0][1];
        var x2 = line[1][0];
        var y2 = line[1][1];
        if (x1 > max_x) max_x = x1;
        if (x2 > max_x) max_x = x2;
        if (y1 > max_y) max_y = y1;
        if (y2 > max_y) max_y = y2;
    }
    return new Array(max_y+1).fill(0).map(() => new Array(max_x+1).fill(0));
}

main();
