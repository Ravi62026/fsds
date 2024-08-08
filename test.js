async function fetchTransactionData(txHash, apiKey) {
    const url = `https://api.etherscan.io/api?module=proxy&action=eth_getTransactionByHash&txhash=${txHash}&apikey=${apiKey}`;
    
    try {
        const response = await fetch(url);
        if (response.ok) {
            const data = await response.json();
            return data;
        } else {
            console.error("Error fetching transaction data:", response.status);
            return null;
        }
    } catch (error) {
        console.error("Error fetching transaction data:", error);
        return null;
    }
}

// Replace 'your_api_key_here' with your actual Etherscan API key
const apiKey = "YGY3NZSZWMY9URGFVBZHHRUIA4215H4SIR";
const txHash = "0x6925d39a08a82ae0121618440e0bd1508e4ba6182b5252ea1875014fb43df14f";

fetchTransactionData(txHash, apiKey)
    .then(txData => {
        if (txData) {
            console.log(txData);
        }
    });
