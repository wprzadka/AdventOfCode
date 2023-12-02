export async function get_input(input_url: string, sessionToken: string){
    const handle: Response = await fetch(input_url, {
        method: "GET",
        headers: {
            'Cookie': 'session='+sessionToken
        },
    });
    return await handle.text();
}