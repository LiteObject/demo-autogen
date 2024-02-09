import autogen

# import OpenAI API Key
config_list = autogen.config_list_from_json(env_or_file="OAI_CONFIG_LIST")

# create the assistant agent
assistant = autogen.AssistantAgent(
    name="assistant", llm_config={"config_list": config_list}
)

# create the user proxy agent
user_proxy = autogen.UserProxyAgent(
    name="userProxy", code_execution_config={"work_dir": "results"}
)

# start the conversation
user_proxy.initiate_chat(
    assistant, message="Write a code to print even numbers from 1 to 100."
)
