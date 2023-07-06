# ML Project Template

## Project File Structure

```sh
.
├── README.md
├── notebook
│   ├── 1.0_author.name_EDA.ipynb
│   └── 1.0_author.name_MODEL_TRAINING.ipynb
├── plots
├── requirements.txt
├── run_mode.config
├── setup.py
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
    │       └── trainer.py
    ├── core
    │   ├── __init__.py
    │   ├── config.py
    │   ├── constants.py
    │   ├── exception.py
    │   ├── file_operation.py
    │   └── logger.py
    ├── database
    │   ├── __init__.py
    │   └── schema.json
    ├── entity
    │   ├── __init__.py
    │   ├── artifact.py
    │   └── config.py
    └── utils
        ├── __init__.py
        └── plot_settings.py
```

## How to Setup

- [setup.py](setup.py)
   - Write the author name and e-mail.
   - Write project name, project description.
   - Provide project version.
- [requirements.txt](requirements.txt)
   - Write all the pip packages required for the project.
- [schema.json](src/database/schema.json)

   - This is dataset schema so fill it with dataset information.

   ```json
   {
     "numberOfColumns": null,
     "columnNames": [],
     "targetColumn": null,
     "numColumnsNames": [],
     "catColumnsNames": []
   }
   ```

- [core](src/core) package
   - It is a package which contains basic required packages of any project like `logger`, `file_operation`, `config`, etc. modules.
- [database](src/database) package
   - This package is used to deal with database to perform operations on database like fetching, inserting and exporting data from database.
- [src.entity.config](src/entity/config.py) module
   - insert all the values which were vary project to project like threshold values, expected training and testing scores, etc.
- [src.core.exception](src/core/exception.py) module
   - If you want change the `CustomException` class name with your personalized name.
- [run_mode.config](run_mode.config)
   - You have to set the `currentRunMode` for the project explicitly because it is important to segregate the **logs** of the project. If you don't do that program automatically set to `training` mode.
- [logger.py](src/core/logger.py)
   - Logger object takes `__name__` argument which makes easy to read the logs.
