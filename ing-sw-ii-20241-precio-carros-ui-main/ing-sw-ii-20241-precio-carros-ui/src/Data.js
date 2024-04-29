const FORM_ENDPOINT = "http://localhost:5000/logic/gates";

const gates = [
    {label: "OR", value: "or"},
    {label: "AND", value: "and"},
    {label: "NOR", value: "nor"},
    {label: "NAND", value: "nand"},
    {label: "XOR", value: "xor"}
]

function getConfig() {
    return {FORM_ENDPOINT, gates};
}

export default getConfig;