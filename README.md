# md-index

A simple Python cli tool to generate a table of contents file from markdown directories

## Setup

```sh
conda create -n md_venv python=3.10 --file requirements.txt
conda activate md_venv
```

## Usage

```sh
python md-index.py generate --directory="./" --target_file="SUMMARY_.md"
```