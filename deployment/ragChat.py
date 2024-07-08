from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv
import os
import boto3
from langchain_community.embeddings.bedrock import BedrockEmbeddings
from langchain_community.llms import Bedrock
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

class ragChat:

    def __init__(self):
        load_dotenv()
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

    def generateReply(self, context_text, query_text) -> str:
        llm = Bedrock(
            model_id="amazon.titan-text-lite-v1",
            client=self.bedrock,
            model_kwargs={
                "maxTokenCount": 1000,
                "stopSequences": [],
                "temperature": 0.7,
                "topP": 1,
            }
        )
        prompt = PromptTemplate(
            input_variables=["context", "question"],
            template=self.PROMPT_TEMPLATE
        )
        chain = LLMChain(llm=llm, prompt=prompt)
        response = chain.run(context=context_text, question=query_text)
        return response
    
    