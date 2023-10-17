# Chatbot

### Description
     This is a Chatbot Web project, development with Django Framework in version: 4.2.2

### Docker

1. Building docker image:
   - <em> Before doing the build, got to file in directory: chatbot/chat/view.py and add the name of the custom model created through instructions in README.md in the project: "chatgpt-api"</em> 
       
    ```bash
      docker build -t chatbot-web:<APP_VERSION> .
    ```

2. Creating the tag:

    ```bash
      docker tag chatbot-web:<APP_VERSION> <TARGET_IMAGE>/chatbot-web:<APP_VERSION>
    ```

3. Run imagem:

    ```bash
      docker run -d -p 8000:8000 chatbot-web:<APP_VERSION>
    ```
