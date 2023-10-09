# ML Project Template

### Project File Structure

<details>
<summary>👀 Click to see!</summary>

```sh
.
├── README.md
├── requirements.txt
└── src
    ├── __init__.py
    ├── components
    │   ├── __init__.py
    │   ├── data
    │   │   ├── __init__.py
    │   │   ├── ingestion.py
    │   │   ├── transformation.py
    │   │   └── validation.py
    │   └── model
    │       ├── __init__.py
    │       ├── evaluation.py
    │       ├── factory.py
    │       └── trainer.py
    ├── core
    │   ├── __init__.py
    │   ├── constants.py
    │   ├── errors.py
    │   ├── io.py
    │   └── logger.py
    ├── database
    │   ├── __init__.py
    │   ├── schema.py
    │   └── schema.yaml
    ├── entity
    │   ├── __init__.py
    │   ├── artifact.py
    │   └── config.py
    └── utils
        └── __init__.py
```

</details>

### Demo Projects

I already build some projects with this project template.

> [!ATTENTION]
>
> They maybe seems irregular with their file structure but they follow this template.

1. [💸 Money Laundering Prevention System](https://github.com/arv-anshul/ineuron-money-laundering)
2. [📦 Products Backorder Prediction](https://github.com/arv-anshul/ineuron-backorder-prediction)
