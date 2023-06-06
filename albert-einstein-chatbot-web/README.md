# Albert Einstein Chatbot

### Description
     This is the Albert Einstein Chatbot Web project, development with Django Framework in version: 4.2.2

### Docker

1. Building docker image:
   - <em> Before doing the build, got to file in directory: chatbot/chat/view.py and add the name of the custom model created through instructions in README.md in the project: "albert-einstein-chatgpt-api"</em> 
       
    ```bash
      docker build -t albert-einstein-chatbot-web:<APP_VERSION> .
    ```

2. Creating the tag:

    ```bash
      docker tag albert-einstein-chatbot-web:<APP_VERSION> <TARGET_IMAGE>/albert-einstein-chatbot-web:<APP_VERSION>
    ```

3. Run imagem:

    ```bash
      docker run -d -p 8000:8000 albert-einstein-chatbot-web:<APP_VERSION>
    ```