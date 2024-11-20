const API_BASE_URL = "http://localhost:8080";

export const classifyEmail = async (text: string): Promise<{ classification: string } | { error: string }> => {
    try {
        const response = await fetch(`${API_BASE_URL}/classify`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text: text }),
        });
        return await response.json();
    } catch (error) {
        return { error: "Failed to classify the email." };
    }
};

export const summarizeEmail = async (text: string): Promise<{ summary: string } | { error: string }> => {
    try {
        const response = await fetch(`${API_BASE_URL}/summarize`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text: text }),
        });
        return await response.json();
    } catch (error) {
        return { error: "Failed to summarize the email." };
    }
};
