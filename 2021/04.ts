import { readFileSync } from 'fs';

const input = readFileSync("./04input").toString().trim().split("\r\n\r\n").map((item) => item.trim());

const numbers = input[0].split(",").map(Number);

function parseBoards(input: string[]): number[][] {
    var result = [];
    for (const board of input.slice(1)) {
        result.push(board.split("\n").map((line) => line.trim().split(/\s+/).map((x) => parseInt(x))))
    }
    return result;
}
const boards = parseBoards(input);

function checker(arr, target): boolean {
    //console.log(arr, target)
    return target.every(v => arr.includes(v));
}

function play() {
    var curr_winner = 1;
    const len = boards.length;
    for (var k = 5; k <= numbers.length; k++) {
        const draw = numbers.slice(0, k);
        for (var b = boards.length-1; b >= 0; b--) {
            var board = boards[b];
            for (var i = 0; i < 5; i++) {
                var hor = [];
                var col = [];
                for (var j = 0; j < 5; j++) {
                    hor.push(board[i][j]);
                    col.push(board[j][i]);
                }
                if (checker(draw, hor) || checker(draw, col)) {
                    //console.log("winning board", board);
                    const winningBoard = [].concat(...board);
                    const winningDraw = draw;
                    const difference = winningBoard.filter(x => !winningDraw.includes(x) );
                    const sum = difference.reduce((sum, current) => sum + current, 0);
                    console.log(curr_winner++, "of", len, "with score", sum*numbers[k-1]);
                    boards.splice(b,1);
                    if (boards.length == 0) {
                        console.log("done");
                        return;
                    }
                    break;
                }
            }
        }
    }
    return -1;
}

play();