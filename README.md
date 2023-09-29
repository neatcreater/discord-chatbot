# Chatbot Service using Large Language Model

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/deep-diver/LLM-As-Chatbot/blob/main/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/deep-diver/LLM-As-Chatbot.svg)](https://github.com/deep-diver/LLM-As-Chatbot/stargazers)

## Table of Contents

- [Update](#update)
- [Introduction](#introduction)
- [Easiest Way to Try Out](#easiest-way-to-try-out)
- [Instructions](#instructions)
- [Context Management](#context-management)
- [Currently Supported Models](#currently-supported-models)
- [Todos](#todos)
- [Acknowledgements](#acknowledgements)

## Update

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

#### Prerequisites

Please note that the code only works with `Python >= 3.9` and `gradio >= 3.32.0`.

```console
$ conda create -n llm-serve python=3.9
$ conda activate llm-serve
