# ChatGPT API Consumer

### Description
    This API is responsible for consume ChatGPT API.

#### Start APP
1. First step is create a virtual environment. In my case, i'm using mkvirtualenv
    
    ```bash
      pip install virtualenvwrapper
    ```

2. Creating environment variables
    
    ```bash
      export WORKON_HOME=~/.virtualenvs
      export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3
   ```
3. Creating the directory where the virtual environments of the applications will be

    ```bash
      mkdir -p $WORKON_HOME
    ```
4. Activate the plugins:
    
    ```bash
      source /usr/local/bin/virtualenvwrapper.sh
    ```

5. To create virtual environment:

    ```bash
      mkvirtualenv <PROJECT_NAME> -p <PYTHON_VERSION>
    ```

6. To activate an existing virtual environment:

    ```bash
      workon <ENVIRONMENT_NAME>
    ```

7. To deactivate an existing virtual environment:

    ```bash
      deactivate
    ```

8. To list all virtual environment:

    ```bash
      lsvirtualenv
    ```

9. To remove a virtual environment:

    ```bash
      rmvirtualenv
    ```

### Documentation

1. The APP's documentation will be in:
   - http://0.0.0.0:3000/docs 



### Docker

1. Building docker image:
    - <em> Before doing the build, add your API Key in the parameter: "CHAT_GPT_API_KEY" 
        inside the .env file that is in the root of the project. </em> 

    ```bash
      docker build -t chatgpt-api:<API_VERSION> .
    ```

2. Creating the tag:

   ```bash
      docker tag chatgpt-api:<API_VERSION> <TARGET_IMAGE>/chatgpt-api:<API_VERSION>
   ```

3. Run imagem:

   ```bash
      docker run -d -p 3000:3000 chatgpt-api:<API_VERSION>
   ```

# Fine Tuning
Creating the ChatGPT template specialization to meet Albert Einstein Academy expectations.

### Instructions:

1. First step, create your account: https://openai.com/
2. Create your ChatGPT API Key in: https://platform.openai.com/account/api-keys.
   <strong> Pay attention to the costs of using the api!! </strong>
3. To execute the steps you need to create an environment variable like:

   ````
   export OPENAI_API_KEY=<CHATGPT_API_KEY>
   ````
   
4. Open the terminal and access this project's directory, then activate the virtual environment. To ensure that the "openai" package is installed, run the command:

   ````
   pip install --upgrade openai
   pip install pandas
   ````

5. In the directory: <strong>app/resources/chatgpt</strong> there is a file <strong>"prepared.jsonl"</strong> with data for training a new model. The idea is to create a specialization of the ChatGPT template: <strong>Davinci</strong>. Access the mentioned directory through the terminal.

### Prepare model in ChatGPT

   ```
   openai tools fine_tunes.prepare_data -f <filename.json>
   ```
   Example:
      ```
      openai tools fine_tunes.prepare_data -f prepared.jsonl
      ```

### Creating model in ChatGPT

```bash
openai api fine_tunes.create -t <filename.json> -m 'model-name'
```
   Example:
```bash
openai api fine_tunes.create -t prepared.jsonl -m davinci
```
   <strong>Obs: </strong> At this time, the processing will enter a queue to be processed. It might take a few minutes.
   In the terminal you will be able to follow the progress of the queue.
   If the terminal loses connection, type the command:
```bash
openai api fine_tunes.follow -i <fine-tune-job-id>
```
   Example:

```bash
openai api fine_tunes.follow -i ft-aODWYQM1dWSr1roOmWuoxYor
```

   When processing is finished, the name of the created model will appear in the terminal.
   This model name is what will be used in API calls. 
   The model's name created: <strong>davinci:ft-personal-2023-06-07-17-17-46</strong>
