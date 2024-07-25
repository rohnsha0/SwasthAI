from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv
import os
import boto3
from langchain_community.embeddings.bedrock import BedrockEmbeddings
from langchain_community.llms import Bedrock
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import openai
from langchain_openai import OpenAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_anthropic import ChatAnthropic


class ragChat:

    def __init__(self, kwargs= None):
        self.errorMessage= ""
        load_dotenv()
        self.SERVICE_NAME= kwargs.get("serviceName", "swasthai")
        self.SECRET_CODE= kwargs.get("secretCode")
        print(kwargs.get("serviceName", "swasthai"))
        os.environ['AWS_DEFAULT_REGION'] = 'ca-central-1'
        self.CHROMA_PATH = "chromaPathology-Copy1"
        self.bedrock= boto3.client('bedrock-runtime', aws_access_key_id= os.environ['ACCESS'], aws_secret_access_key=os.environ['SECRET'])
        self.PROMPT_TEMPLATE= """
Hello! I'm SwasthAI Chat, I am here to help answer your medical questions based on specific context. Here's how our interaction will work:

1. I'll first provide you with some relevant medical context.
2. Then, you can ask your medical question.
3. I'll answer based solely on the given context if it's a medical query.

Let's begin:

Context:
{context}

---

Now, what medical question would you like to ask about this topic? Please note that I can only address medical queries related to the context provided above.

Your question: {question}

[INTERNAL INSTRUCTION: Analyze if the question is a medical query related to the given context. If it is, proceed with answering. If not, provide a polite refusal message.]

My response:
"""
        print("Loading Chatbot...")


    def get_response(self, query_text) -> str:
        db = Chroma(persist_directory=self.CHROMA_PATH, embedding_function=self.get_embedding_function())
        results = db.similarity_search_with_relevance_scores(query_text, k=3)
        context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
        return self.generateReply(context_text=context_text, query_text=query_text)
    
    def get_embedding_function(self):
        return BedrockEmbeddings(client=self.bedrock, model_id="amazon.titan-embed-text-v2:0")
    
    def get_llm(self):
        if self.SERVICE_NAME == "swasthai":
            return Bedrock(
            model_id="amazon.titan-text-lite-v1",
            client=self.bedrock,
            model_kwargs={
                "maxTokenCount": 1000,
                "stopSequences": [],
                "temperature": 0.7,
                "topP": 1,
            }
        )
        if self.SERVICE_NAME=="openai":
            return ChatOpenAI(
            api_key=self.SECRET_CODE,
            model="gpt-4o-mini",
            )
        
        if self.SERVICE_NAME=="google":
            return ChatGoogleGenerativeAI(google_api_key=self.SECRET_CODE, model="gemini-1.5-flash")
        
        if self.SERVICE_NAME=="anthropic":
            return ChatAnthropic(api_key=self.SECRET_CODE, model="claude-3-haiku-20240307")

        return Bedrock(
            model_id="amazon.titan-text-lite-v1",
            client=self.bedrock,
            model_kwargs={
                "maxTokenCount": 1000,
                "stopSequences": [],
                "temperature": 0.7,
                "topP": 1,
            }
        )

    def generateReply(self, context_text, query_text) -> str:
        llm = self.get_llm()
        prompt = PromptTemplate(
            input_variables=["context", "question"],
            template=self.PROMPT_TEMPLATE
        )
        chain = LLMChain(llm=llm, prompt=prompt)
        response = chain.run(context=context_text, question=query_text)
        return response