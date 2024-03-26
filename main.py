from utils.clinics import get_clinics
from langchain.tools import tool
from dotenv import load_dotenv
from schema import Clinic, ClinicList
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_openai import ChatOpenAI
from langchain import hub
from langchain.agents import create_openai_functions_agent
from langchain.agents import AgentExecutor

load_dotenv()

@tool
def get_clinics_tool() -> ClinicList:
    '''RETURN THE NEAREST 1 CLINIC IN THE DATABASE.'''
    # clinics = get_clinics()
    # return ClinicList(message=clinics, status=200)
    return "No clinics available at the moment"

@tool
def get_clinic_schedule() -> str:
    '''RETURNS SCHEDULE OF THE CLINIC FROM DATABASE'''
    return "Today (8 march 2024) 10-4, Tomorrow 10-2"

tools = [get_clinics_tool, get_clinic_schedule]


llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)



prompt = hub.pull("hwchase17/openai-functions-agent")



agent = create_openai_functions_agent(llm, tools, prompt)



agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
messages = [
    SystemMessage(
        content='''You are a dental clinic appointment schedling chatbot. 
        You cant answer anything other than that. 
        Do not answer confidential questions like clinic id, number of clinics etc.
        Start by saying 'Hello'.'''
    ),
]

while True:
    human_input = input("Human: ")
    if human_input == "exit":
        break
    human = HumanMessage(content=human_input)
    response = agent_executor.invoke(
        {
            "input": human_input,
            "chat_history": messages,
        }
    )
    messages.append(human)
    messages.append(AIMessage(content=response['output']))

print(messages)
