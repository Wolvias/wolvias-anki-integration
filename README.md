# Wolvias Anki Integration

Anki integration for **WA-PDF Studio**.

This add-on allows Anki to display questions exported from WA-PDF Studio, including their PDF image and annotation rectangles.

## Features

* Displays WA-PDF Studio questions inside Anki
* Renders the exported PDF image
* Displays annotation rectangles on the image
* Supports question and answer cards
* Supports Anki's card preview
* Compatible with WA-PDF Studio `.apkg` exports
* Keeps the processing inside Anki — no external service is required

## Requirements

* Anki **23.10 or newer**
* An `.apkg` file exported from **WA-PDF Studio**

## Installation

### Option 1 — AnkiWeb

If the add-on is available on AnkiWeb:

1. Open Anki.
2. Go to **Tools → Add-ons → Get Add-ons**.
3. Enter the add-on code.
4. Restart Anki.

### Option 2 — Install from file

1. Download the latest `.ankiaddon` file from the [Releases](../../releases) page.
2. Open Anki.
3. Go to **Tools → Add-ons → Install from file**.
4. Select the downloaded `.ankiaddon` file.
5. Restart Anki.

## Usage

1. Create or open a project in **WA-PDF Studio**.
2. Create your PDF questions and annotations.
3. Export the questions as an **Anki package (`.apkg`)**.
4. Import the `.apkg` file into Anki.
5. Review the cards normally.

The add-on automatically detects Wolvias PDF Question cards and renders their annotation rectangles.

## Compatibility

The add-on expects cards exported by WA-PDF Studio using the following fields:

* `Question`
* `Image`
* `Rectangles`

Older Wolvias rectangle markers are also supported for compatibility.

## Troubleshooting

### The rectangles are not displayed

Make sure:

* The card was exported from WA-PDF Studio.
* The `Rectangles` field contains valid data.
* The add-on is enabled.
* You restarted Anki after installing or updating the add-on.

### Anki shows an error

Please include the error message and your Anki version when reporting an issue.

## About

**Wolvias Anki Integration** is part of the Wolvias ecosystem.

WA-PDF Studio is a browser-based PDF annotation and study tool.

**WA-PDF Studio:** [Coming soon / official link]

## License

See the repository for licensing information.
