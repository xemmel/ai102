import os
import json
from dotenv import load_dotenv

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition, FunctionTool
from openai.types.responses.response_input_param import FunctionCallOutput, ResponseInputParam

from functions import rewrite_text, rewrite_text2

def main():
    os.system('cls' if os.name=='nt' else 'clear')
    print("Starting")
    load_dotenv()    
    project_endpoint = os.getenv("PROJECT_ENDPOINT")
    model_deployment = os.getenv("MODEL_DEPLOYMENT_NAME")
    
    rewrite_text_tool = FunctionTool(
        name = "rewrite_text_tool",
        description="Rewrite whatever is in input_text",
        parameters={
        "type": "object",
        "properties": {
            "input_text": {
                "type": "string",
                "description": "The input text to rewrite should be placed here",
            },
        },
        "required": ["input_text"],
        "additionalProperties": False,
    },
    strict=True,
    )

    rewrite2_text_tool = FunctionTool(
        name = "rewrite2_text_tool",
        description="Rewrite2 whatever is in input_text",
        parameters={
        "type": "object",
        "properties": {
            "input_text": {
                "type": "string",
                "description": "The input text to rewrite2 should be placed here",
            },
        },
        "required": ["input_text"],
        "additionalProperties": False,
    },
    strict=True,
    )
    
    with (
     DefaultAzureCredential() as credential,
     AIProjectClient(endpoint=project_endpoint, credential=credential) as project_client,
     project_client.get_openai_client() as openai_client,
    ):

        agent = project_client.agents.create_version(
            agent_name="morten2",
            definition=PromptAgentDefinition(
            model=model_deployment,
            instructions=
                """You are a chatbot""",
            tools=[ rewrite_text_tool, rewrite2_text_tool ],
            ),
        )
        ## agent = project_client.agents.create_version("morten2")

        conversation = openai_client.conversations.create()
        input_list: ResponseInputParam = []        
        while True:

            user_input = input("Enter a prompt for the astronomy agent. Use 'quit' to exit.\nUSER: ").strip()
            if user_input.lower() == "quit":
                print("Exiting chat.")
                break

            openai_client.conversations.items.create(
                conversation_id=conversation.id,
                items=[{"type": "message", "role": "user", "content": user_input}],
            )
            roundtrip_needed = True
            previous_response_id = None
            while roundtrip_needed:
                roundtrip_needed = False
                if previous_response_id:
                    response = openai_client.responses.create(
                        extra_body={"agent": {"name": agent.name, "type": "agent_reference"}},
                        previous_response_id=previous_response_id,
                        input=input_list,
                    )
                else:
                    response = openai_client.responses.create(
                        conversation=conversation.id,
                        extra_body={"agent": {"name": agent.name, "type": "agent_reference"}},
                        input=input_list,
                    )
                previous_response_id = response.id
                if response.status == "failed":
                    print(f"Response failed: {response.error}")

                for item in response.output:
                    if item.type == "function_call":
                        roundtrip_needed = True
                        function_name = item.name
                        result = None
                        if (item.name == "rewrite_text_tool"):
                            result = rewrite_text(**json.loads(item.arguments))
                        elif (item.name == "rewrite2_text_tool"):
                            result = rewrite_text2(**json.loads(item.arguments))
                        input_list.append(
                            FunctionCallOutput(
                            type="function_call_output",
                            call_id=item.call_id,
                            output=result,
                        )
                )
            ## Send to final!! response call
            # if input_list:
            #     response = openai_client.responses.create(
            #         input=input_list,
            #         previous_response_id=response.id,
            #         extra_body={"agent": {"name": agent.name, "type": "agent_reference"}},
            #     )
            # Display the agent's response
            print(f"AGENT: {response.output_text}")

if __name__ == "__main__":
    main()