from dotenv import load_dotenv

load_dotenv()

from langchain import hub
from langchain.agents import AgentExecutor
from langchain.agents.react.agent import create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch

tools = [TavilySearch()]
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.1,  # Reduzir temperatura para respostas mais consistentes
    max_tokens=4096,  # Aumentar contexto se necessário
    top_p=0.9,
    top_k=40
)
# Prompt personalizado mais claro para o Gemini
react_prompt = hub.pull("hwchase17/react")

# Modificar o prompt para ser mais específico sobre o formato esperado
from langchain.prompts import PromptTemplate

custom_prompt = PromptTemplate.from_template("""
Você é um assistente útil que pode usar ferramentas para responder perguntas.
Você DEVE seguir este formato exato:

Thought: [seu pensamento sobre o que fazer]
Action: [nome da ferramenta]
Action Input: [entrada para a ferramenta]
Observation: [resultado da ferramenta]
... (este Thought/Action/Action Input/Observation pode repetir N vezes)
Thought: [seu pensamento final sobre a resposta]
Final Answer: [sua resposta final]

Ferramentas disponíveis:
{tools}

Formato de entrada da ferramenta:
{tool_names}

Pergunta: {input}

{agent_scratchpad}
""")

agent = create_react_agent(
    llm=llm, 
    tools=tools, 
    prompt=custom_prompt
)
agent_executor = AgentExecutor(
    agent=agent, 
    tools=tools, 
    verbose=True,
    handle_parsing_errors=True
)
chain = agent_executor

def main():
    try:
        result = chain.invoke(
            input={
                "input": "search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details",
            }
        )
        print("Resultado da busca:")
        print(result)
    except Exception as e:
        print(f"Erro durante a execução: {e}")
        print("Verificando se o modelo Gemini está funcionando...")
        
        # Teste simples do LLM
        try:
            test_response = llm.invoke("Olá, você está funcionando?")
            print(f"Teste do LLM: {test_response.content}")
            
            # Teste específico do formato ReAct
            print("\nTestando formato ReAct...")
            react_test = llm.invoke("""
Thought: Preciso responder uma pergunta simples.
Final Answer: Esta é uma resposta de teste.
""")
            print(f"Teste ReAct: {react_test.content}")
            
        except Exception as llm_error:
            print(f"Erro no LLM: {llm_error}")
            print("Verifique se a API key do Google está configurada corretamente")
            print("Certifique-se de ter a variável GOOGLE_API_KEY no seu arquivo .env")
            print("Para obter uma API key: https://makersuite.google.com/app/apikey")


if __name__ == "__main__":
    main()
