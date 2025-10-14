from dotenv import load_dotenv

load_dotenv()

from langchain import hub
from langchain.agents import AgentExecutor
from langchain.agents.react.agent import create_react_agent
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch

tools = [TavilySearch()]
llm = ChatOllama(model="gpt-oss:20b")
react_prompt = hub.pull("hwchase17/react")
agent = create_react_agent(
    llm=llm, 
    tools=tools, 
    prompt=react_prompt
)
agent_executor = AgentExecutor(
    agent=agent, 
    tools=tools, 
    verbose=True,
    handle_parsing_errors=True,
    max_iterations=5
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
        print("Verificando se o modelo Ollama está funcionando...")
        
        # Teste simples do LLM
        try:
            test_response = llm.invoke("Olá, você está funcionando?")
            print(f"Teste do LLM: {test_response.content}")
        except Exception as llm_error:
            print(f"Erro no LLM: {llm_error}")
            print("Verifique se o Ollama está rodando e o modelo 'gpt-oss:20b' está disponível")


if __name__ == "__main__":
    main()
