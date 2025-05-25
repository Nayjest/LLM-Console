<p align="right">
<a href="https://pypi.org/project/llm-console/" target="_blank"><img src="https://badge.fury.io/py/llm-console.svg" alt="PYPI Release"></a>
<a href="https://github.com/Nayjest/LLM-Console/actions/workflows/code-style.yml" target="_blank"><img src="https://github.com/Nayjest/LLM-Console/actions/workflows/code-style.yml/badge.svg" alt="Code Style"></a>
<a href="https://github.com/Nayjest/LLM-Console/actions/workflows/tests.yml" target="_blank"><img src="https://github.com/Nayjest/LLM-Console/actions/workflows/tests.yml/badge.svg" alt="Tests"></a>
<a href="https://github.com/Nayjest/LLM-Console/blob/main/LICENSE" target="_blank"><img src="https://img.shields.io/static/v1?label=license&message=MIT&color=d08aff" alt="License"></a>
</p>

# LLM-Console

**LLM-Console** is a cross-platform vendor-agnostic command-line interface for LLMs.

**Development Status**: bookmark it and go away, it is still in early development.

## ✨ Features

- @todo
- Flexible configuration via [`.env` file](https://github.com/Nayjest/LLM-Console/blob/main/.env.example)
- Extremely fast, parallel LLM usage
- Model-agnostic (OpenAI, Anthropic, Google, local PyTorch inference, etc.)


## 🚀 Quickstart
```bash
# Install LLM Console via pip
pip install llm-console

# Run the interactive wizard to configure the connection to your language model.
llm

# Talk to your Language Model
llm "Wazzup, LLM"
```

## Usage Examples

```bash
llm --mcp https://time.mcp.inevitable.fyi/mcp what is current time in Ukraine? answer in H:i:s, no additional text
> 16:31:12
```

```
>llm --mcp https://time.mcp.inevitable.fyi/mcp H:i time across a Europe, in valid toml, no text before of after toml
[EuropeTime]
London = "2024-06-10T13:38:23+01:00"
Paris = "2024-06-10T14:38:23+02:00"
Berlin = "2024-06-10T14:38:23+02:00"
Madrid = "2024-06-10T14:38:23+02:00"
Rome = "2024-06-10T14:38:23+02:00"
Athens = "2024-06-10T15:38:23+03:00"
Istanbul = "2024-06-10T16:38:23+03:00"
```

## 🤝 Contributing

We ❤️ contributions! See [CONTRIBUTING.md](CONTRIBUTING.md).

## 📝 License

Licensed under the [MIT License](LICENSE).

© 2022&mdash;2025 [Vitalii Stepanenko](mailto:mail@vitaliy.in)
