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
    for (let row of rows) {
        if (row === "") continue;
        let matches = row.match(/\d/g);
        if (!matches) throw("wrong regex value for \|" + row + "\|");
        sum += Number(matches[0] + matches[matches.length - 1]);
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
}

main();