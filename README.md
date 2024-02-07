# Demo AutoGen Studio

AutoGen Studio is an interface powered by AutoGen, a framework developed by Microsoft for orchestrating multi-agent workflows. It provides a user-friendly environment for rapidly prototyping and managing agents that can learn, adapt, and collaborate.

## Key Features of AutoGen Studio:
- Declarative Agent and Workflow Definition: AutoGen Studio allows users to define and modify agents and multi-agent workflows through a point-and-click, drag-and-drop interface. Users can select the parameters of agents and specify how they communicate to solve tasks.

- Interactive Chat Sessions: Users can create chat sessions with specified agents and view the results. The interface provides features such as viewing chat history, generated files, and time taken.

- Skill Integration: AutoGen Studio enables users to explicitly add skills to agents, allowing them to accomplish more tasks. Skills are functions that describe how to solve a task, and they can be added to AutoGen Studio via the provided UI.

- Local Gallery: Users can publish their sessions to a local gallery, facilitating sharing and reusing of artifacts such as workflow configurations and sessions.

## Getting Started with AutoGen Studio:

- Installation: The recommended installation option for AutoGen setup is to use Docker. Here are the step-by-step instructions to install AutoGen using Docker:
  - First, make sure you have Docker installed on your system.
  - Once Docker is installed, you can build a Docker image for AutoGen. AutoGen provides pre-configured Dockerfiles for different needs. 
  
  ### For a basic setup, you can use the autogen_base_img.

        docker build -f .devcontainer/Dockerfile -t autogen_base_img https://github.com/microsoft/autogen.git
  
  ### For advanced features, you can use the autogen_full_img. Use the appropriate Docker build command based on your needs:

        docker build -f .devcontainer/full/Dockerfile -t autogen_full_img https://github.com/microsoft/autogen.git

  ### After building the Docker image, you can run AutoGen applications from the Docker image. Use the `docker run` command, and make sure to mount your local application directory to the Docker container. Here's an example command to run an application built with AutoGen:

        docker run -it -v $(pwd)/myapp:/home/autogen/autogen/myapp autogen_base_img:latest python /home/autogen/autogen/myapp/main.py

  In this example, `$(pwd)/myapp` is your local directory, and `/home/autogen/autogen/myapp` is the path in the Docker container where your code will be located.

  For more information, [click here](https://microsoft.github.io/autogen/docs/installation/Docker).

- Configure an LLM Provider: You need access to a language model, and you can set this up by following the steps in the AutoGen documentation. You can configure your environment with either OPENAI_API_KEY or AZURE_OPENAI_API_KEY.

## Exploring AutoGen Studio:
- Build: This section focuses on defining the properties of agents and agent workflows. Users can view, add, or edit skills that an agent can leverage in addressing tasks. They can also specify agent properties and define agent workflows.

- Playground: In this section, users can interact with agent workflows defined in the Build section. They can collaborate with agents, use available skills, and address user tasks. The Playground section includes concepts such as sessions and chat views.

- Gallery: The Gallery section is focused on sharing and reusing artifacts such as workflow configurations and sessions.
