import "dotenv/config"

async function get_input(input_url: string, sessionToken: string){
    const handle: Response = await fetch(input_url, {
        method: "GET",
        headers: {
            'Cookie': 'session='+sessionToken
        },
    });
    return await handle.text();
}

function solve(data: string): number {
    let sum: number = 0;
    let rows: string[] = data.split("\n");
    const regex = /(?=(\d|one|two|three|four|five|six|seven|eight|nine))/g;
    const words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
    for (let row of rows) {
        if (row === "") continue;
        let matches = Array.from(row.matchAll(regex), x => x[1]);
        if (!matches) throw("wrong regex value for \|" + row + "\|");
        function mapToDigit(word: string): string {
            return word.length == 1 ? word : (words.indexOf(word) + 1).toString();
        }
        const fst = mapToDigit(matches[0]);
        const snd = mapToDigit(matches[matches.length - 1]);
        console.log(row, Number(fst + snd));
        console.log(matches)
        sum +=  Number(fst + snd);
    }
    return sum;
}

function main() {
    const input_url: string = "https://adventofcode.com/2023/day/1/input";
    const sessionToken = process.env.AOC_SESSION_TOKEN

    Promise.resolve(get_input(input_url, sessionToken)
        .then(data => console.log(solve(data)))
        .catch(err => console.log("error: " + err))
    );

    const example = `two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen`;

    console.log(solve(example))
}

main();