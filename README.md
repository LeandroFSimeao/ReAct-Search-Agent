# ReAct Search Agent - LangChain Course

Este projeto implementa um agente ReAct (Reasoning and Acting) usando LangChain, que combina capacidades de raciocínio com busca web para resolver problemas complexos.

## 🚀 Características

- **Agente ReAct**: Implementa o padrão Reasoning and Acting para tomada de decisões inteligentes
- **Busca Web Integrada**: Utiliza TavilySearch para acessar informações em tempo real da internet
- **Suporte a Múltiplos Modelos**: Compatível com modelos Ollama e outros provedores de LLM
- **Framework LangChain**: Aproveita a robustez e flexibilidade do LangChain

## 🛠️ Tecnologias Utilizadas

- **LangChain**: Framework principal para desenvolvimento com LLM
- **TavilySearch**: API de busca web para informações atualizadas
- **ChatOllama**: Integração com modelos Ollama
- **Python 3.13+**: Linguagem de programação base

## 📋 Pré-requisitos

- Python 3.13 ou superior
- Conta no TavilySearch (para busca web)
- Modelo Ollama configurado (opcional)

## ⚙️ Instalação

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd langchain-course
```

2. Instale as dependências usando uv:
```bash
uv sync
```

3. Configure as variáveis de ambiente:
```bash
cp .env.example .env
# Edite o arquivo .env com suas chaves de API
```

## 🚀 Como Usar

Execute o projeto:
```bash
uv run python main.py
```

## 📁 Estrutura do Projeto

```
langchain-course/
├── main.py              # Arquivo principal com implementação do agente
├── pyproject.toml       # Configurações do projeto e dependências
├── uv.lock             # Lock file das dependências
└── README.md           # Documentação do projeto
```

## 🔧 Configuração

O projeto utiliza as seguintes variáveis de ambiente:

- `TAVILY_API_KEY`: Chave da API do TavilySearch para busca web
- `OLLAMA_BASE_URL`: URL base do servidor Ollama (opcional)

## 📚 Conceitos do ReAct

O padrão ReAct (Reasoning and Acting) permite que o agente:

1. **Reason (Raciocinar)**: Analisa o problema e planeja a próxima ação
2. **Act (Agir)**: Executa a ação planejada (ex: busca web, processamento)
3. **Observe (Observar)**: Avalia o resultado da ação

Este ciclo se repete até que o problema seja resolvido.

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para:

- Reportar bugs
- Sugerir novas funcionalidades
- Enviar pull requests
- Melhorar a documentação

## 📄 Licença

Este projeto é parte de um curso sobre LangChain e está disponível para fins educacionais.
