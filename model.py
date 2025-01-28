from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_groq import ChatGroq

llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    temperature=0
)

systemPrompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You name is Julian. You help out people with your coding knowledge. Your answer is always concise."
        ),
        ("human", "{input}")
    ]
)

chat = systemPrompt | llm