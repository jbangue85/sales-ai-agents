import { ChatOpenAI } from "@langchain/openai";

const model = new ChatOpenAI({
    openAIApiKey: ""
}

)

const response = await model.invoke("Hello");
console.log(response);