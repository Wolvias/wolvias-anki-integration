# Wolvias Anki Integration

Anki integration for **WA-PDF Studio**.

This add-on allows Anki to display questions exported from WA-PDF Studio, including their PDF image and annotation rectangles.

## Features

* Displays WA-PDF Studio questions inside Anki
* Renders PDF images
* Displays annotation rectangles on the images
* Supports question and answer cards
* Supports Anki card preview
* Automatically detects Wolvias PDF Question cards
* Supports `.apkg` exports from WA-PDF Studio

## Requirements

* Anki 23.10 or newer
* An `.apkg` file exported from WA-PDF Studio

## Installation

This add-on is currently distributed as a folder.

1. Download the repository.
2. Extract the repository files.
3. Copy the add-on folder to your Anki add-ons directory:

```text
Anki2/addons21/
```

The final structure should look like:

```text
Anki2/
└── addons21/
    └── wolvias_anki/
        ├── __init__.py
        ├── constants.py
        ├── renderer.py
        └── manifest.json
```

4. Restart Anki.

## Usage

1. Create your questions and annotations in **WA-PDF Studio**.
2. Export them as an **Anki package (`.apkg`)**.
3. Import the `.apkg` file into Anki.
4. Review the cards normally.

The add-on automatically detects Wolvias PDF Question cards and renders their annotation rectangles.

## How It Works

WA-PDF Studio exports the required information into the Anki card fields.

The add-on reads these fields and renders the PDF image and annotation rectangles when the card is displayed.

The expected fields are:

* `Question`
* `Image`
* `Rectangles`

No external service is required for the add-on.

## Compatibility

The add-on supports:

* Review cards
* Answer cards
* Card preview
* Current WA-PDF Studio rectangle format
* Legacy Wolvias rectangle markers

## Troubleshooting

### The rectangles are not displayed

Make sure:

* The card was exported from WA-PDF Studio.
* The `Rectangles` field contains valid data.
* The add-on folder is inside `Anki2/addons21/`.
* Anki has been restarted after installing the add-on.

### Anki shows an error

Please include:

* Your Anki version
* The error message
* The version of Wolvias Anki Integration

when reporting an issue.

## About

**Wolvias Anki Integration** is an add-on for **WA-PDF Studio**, a browser-based PDF annotation and study tool developed by Wolvias.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
