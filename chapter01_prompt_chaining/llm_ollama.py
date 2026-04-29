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


def test_ollama_stream():
    llm = ChatOllama(
        model="qwen3:4b",
        base_url="http://10.100.16.18:11434/",
        temperature=0.7,
    )
    # 如果使用普通模型，可以在提示词中明确要求展示思考过程
    user_input = "请详细展示你的思考过程，然后再回答：为什么地球是圆的？"
    
    print("AI 正在思考并输出：")
    # 使用 stream 方法流式输出，并且设置 end="" 避免字符串换行
    for chunk in llm.stream(user_input):
        print(chunk.content, end="", flush=True)
    print()


def main():
    # test_ollama()
    test_ollama_stream()


if __name__ == "__main__":
    main()
