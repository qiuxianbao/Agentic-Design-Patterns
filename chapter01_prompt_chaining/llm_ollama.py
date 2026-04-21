from langchain_ollama import ChatOllama


def test_ollama():
    llm = ChatOllama(
        model="gemma2:2b",
        base_url="http://localhost:11434/",
        temperature=0.7,
    )
    user_input = "介绍一下你自己"
    response = llm.invoke(user_input)
    print(response.content)


def main():
    test_ollama()


if __name__ == "__main__":
    main()
