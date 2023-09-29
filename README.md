# Chatbot Service using Large Language Model

## Services

- **Internet Search Support**: You can enable **internet search** capability in the Gradio application and Discord bot. For Gradio, there is an `internet mode` option in the control panel. For Discord, you need to specify the `--internet` option in your prompt. For both cases, you need a Serper API Key, which you can obtain from [serper.dev](https://serper.dev/). By signing up, you will get 2,500 free Google searches, which is sufficient for long-term testing.
- **Discord Bot Support**: You can serve any model from the model zoo as a Discord Bot. Find instructions on how to do this in the section below.

## Introduction

The purpose of this repository is to provide access to a variety of open-source instruction-following fine-tuned LLM (Large Language Model) models as a Chatbot service. Since different models behave differently and require differently formatted prompts, a simple library called [`Ping Pong`](https://github.com/deep-diver/PingPong) has been created for model-agnostic conversation and context management. Additionally, [`GradioChat`](https://github.com/deep-diver/gradio-chat) UI has been developed, which has a similar interface to [HuggingChat](https://huggingface.co/chat/), entirely built in Gradio. These two projects are fully integrated to power this project.

## Easiest Way to Try Out (✅ Gradio, 🚧 Discord Bot)

### Jarvislabs.ai

This project is available as one of the default frameworks at [jarvislabs.ai](https://jarvislabs.ai/). Jarvislabs.ai is a cloud GPU VM provider with competitive GPU prices. Moreover, all the weights of the supported popular open-source LLMs are pre-downloaded. You can try out any model in less than 10 minutes. For further instructions on running the Gradio application, please refer to the [official documentation](https://jarvislabs.ai/docs/llmchat) for the `llmchat` framework.

### dstack

[`dstack`](https://dstack.ai) is an open-source tool that allows you to run LLM-based apps in a cloud of your choice with a single command. `dstack` supports AWS, GCP, Azure, Lambda Cloud, and more. Use the `gradio.dstack.yml` and `discord.dstack.yml` configurations to run the Gradio app and Discord bot via `dstack`. For more details on how to run this repo with `dstack`, read the [official documentation](https://dstack.ai/examples/llmchat) provided by `dstack`.

## Instructions

### Standalone Gradio App

![Gradio App Screenshot](https://i.ibb.co/gW7yKj9/2023-05-26-3-31-06.png)

1. Prerequisites

    Note that the code only works `Python >= 3.9` and `gradio >= 3.32.0`

    ```console
    $ conda create -n llm-serve python=3.9
    $ conda activate llm-serve
    ```

2. Install dependencies. 
    ```console
    $ cd LLM-As-Chatbot
    $ pip install -r requirements.txt
    ```

3. Run Gradio application

    There is no required parameter to run the Gradio application. However, there are some small details worth being noted. When `--local-files-only` is set, application won't try to look up the Hugging Face Hub(remote). Instead, it will only use the files already downloaded and cached.

    Hugging Face libraries stores downloaded contents under `~/.cache` by default, and this application assumes so. However, if you downloaded weights in different location for some reasons, you can set `HF_HOME` environment variable. Find more about the [environment variables here](https://huggingface.co/docs/huggingface_hub/package_reference/environment_variables)

   In order to leverage **internet search** capability, you need Serper API Key. You can set it manually in the control panel or in CLI. When specifying the Serper API Key in CLI, it will be injected into the corresponding UI control. If you don't have it yet, please get one from [serper.dev](https://serper.dev/). By signing up, you will get free 2,500 free google searches which is pretty much sufficient for a long-term test.

    ```console
    $ python app.py --root-path "" \
                    --local-files-only \
                    --share \
                    --debug \
                    --serper-api-key "YOUR SERPER API KEY"
    ```

### Discord Bot

![](https://i.ibb.co/cJ3yDWh/2023-07-14-1-42-23.png)

1. Prerequisites

    Note that the code only works `Python >= 3.9` 

    ```console
    $ conda create -n llm-serve python=3.9
    $ conda activate llm-serve
    ```

2. Install dependencies. 
    ```console
    $ cd LLM-As-Chatbot
    $ pip install -r requirements.txt
    ```

3. Run Discord Bot application. Choose one of the modes in `--mode-[cpu|mps|8bit|4bit|full-gpu]`. `full-gpu` will be choseon by default(`full` means `half` - consider this as a typo to be fixed later).

    The `--token` is a required parameter, and you can get it from [Discord Developer Portal](https://discord.com/developers/docs/intro). If you have not setup Discord Bot from the Discord Developer Portal yet, please follow [How to Create a Discord Bot Account](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/) section of the tutorial from [freeCodeCamp](https://www.freecodecamp.org/) to get the token.

    The `--model-name` is a required parameter, and you can look around the list of supported models from [`model_cards.json`](https://github.com/deep-diver/LLM-As-Chatbot/blob/main/model_cards.json).

    `--max-workers` is a parameter to determine how many requests to be handled concurrently. This simply defines the value of the `ThreadPoolExecutor`.

    When `--local-files-only` is set, application won't try to look up the Hugging Face Hub(remote). Instead, it will only use the files already downloaded and cached.

   In order to leverage **internet search** capability, you need Serper API Key. If you don't have it yet, please get one from [serper.dev](https://serper.dev/). By signing up, you will get free 2,500 free google searches which is pretty much sufficient for a long-term test. Once you have the Serper API Key, you can specify it in `--serper-api-key` option.
   
    - Hugging Face libraries stores downloaded contents under `~/.cache` by default, and this application assumes so. However, if you downloaded weights in different location for some reasons, you can set `HF_HOME` environment variable. Find more about the [environment variables here](https://huggingface.co/docs/huggingface_hub/package_reference/environment_variables)    

    ```console
    $ python discord_app.py --token "DISCORD BOT TOKEN" \
                            --model-name "alpaca-lora-7b" \
                            --max-workers 1 \
                            --mode-[cpu|mps|8bit|4bit|full-gpu] \
                            --local_files_only \
                            --serper-api-key "YOUR SERPER API KEY"
    ```

4. Supported Discord Bot commands

    There is no slash commands. The only way to interact with the deployed discord bot is to mention the bot. However, you can pass some special strings while mentioning the bot.

    - **`@bot_name help`**: it will display a simple help message
    - **`@bot_name model-info`**: it will display the information of the currently selected(deployed) model from the [`model_cards.json`](https://github.com/deep-diver/LLM-As-Chatbot/blob/main/model_cards.json).
    - **`@bot_name default-params`**: it will display the default parameters to be used in model's `generate` method. That is `GenerationConfig`, and it holds parameters such as `temperature`, `top_p`, and so on.
    - **`@bot_name user message --max-new-tokens 512 --temperature 0.9 --top-p 0.75 --do_sample --max-windows 5 --internet`**: all parameters are used to dynamically determine the text geneartion behaviour as in `GenerationConfig` except `max-windows`. The `max-windows` determines how many past conversations to look up as a reference. The default value is set to `3`, but as the conversation goes long, you can increase this value. `--internet` will try to answer to your prompt by aggregating information scraped from google search. To use `--internet` option, you need to specify `--serper-api-key` when booting up the program.
