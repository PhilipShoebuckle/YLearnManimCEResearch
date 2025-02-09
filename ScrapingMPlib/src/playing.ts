import axios from "axios";
import cheerio from "cheerio";

const url = "https://www.premierleague.com/tables";
const AxiosInstance = axios.create();

interface teamData {
    name: string;
}

AxiosInstance.get(url)
.then(response => {
    const html = response.data;
    const $ = cheerio.load(html);
    const rankingsTableRows = $(".tableMid > ")
    console.log(html);
}).catch(console.error);