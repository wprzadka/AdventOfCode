import { get_input } from "../utils/get_input";
import "dotenv/config"

function solve(data: string): number {
    let sum: number = 0;
    for (let row of data.split(/Game \d+: /)) {
        if (row === "") continue;
        console.log(row);
        const min_vals: Map<string, number> = new Map([["red", 0], ["green", 0], ["blue", 0]]);

        for (let word of row.split(/,|;/g)) {
            let entities = word.trim().split(" ");
            let value = Number(entities[0]);
            let color = entities[1];

            if (value > min_vals.get(color)) {
                min_vals.set(color, value);
            }
        }
        sum += Array.from(min_vals.values()).reduce((a, b) => a * b, 1);
    }
    return sum;
}

function main() {
    const input_url: string = "https://adventofcode.com/2023/day/2/input";
    const sessionToken = process.env.AOC_SESSION_TOKEN
    console.log(sessionToken)

    Promise.resolve(get_input(input_url, sessionToken)
        .then(data => console.log(solve(data)))
        .catch(err => console.log("error: " + err))
    );

    const example = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
        + "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"
        + "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
        + "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"
        + "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green";
    console.log(solve(example));
}

main();