# Convert RGB to OKLCH

This project provides a Python implementation to convert RGB color values into the OKLCH color space, a modern color representation adopted in Tailwind CSS V4. By utilizing the `python-oklch` library, this tool extracts colors from the Tailwind CSS documentation and converts them into OKLCH format.

## Features

-   **Web scraping**: Automatically extracts RGB colors from the Tailwind CSS documentation.
-   **RGB to OKLCH conversion**: Leverages the `python-oklch` library for precise color conversion.
-   **Output formatting**: Presents colors in a rounded OKLCH format (`oklch(L% C H)`).

## Dependencies

The script requires the following Python packages:

-   `beautifulsoup4`: For parsing HTML and extracting data.
-   `requests`: To fetch the Tailwind CSS documentation.
-   `python-oklch`: For converting RGB to OKLCH.
-   `lxml`: As the parser for BeautifulSoup.

You can install all dependencies using `pip`:

```bash
pip install beautifulsoup4 requests lxml
```

## Usage

### How it works

1. **Scrape the Tailwind CSS documentation**: The script fetches the HTML content of the Tailwind background color documentation.
2. **Extract color information**: It parses the table containing RGB colors for different shades of colors.
3. **Convert to OKLCH**: Each RGB color is converted into OKLCH format.
4. **Store results in a dictionary**: Colors are organized by name and shade, e.g., `{ "red": { "50": "oklch(97% 0.12 23)", ... } }`.

### Output

The final output is a dictionary containing the OKLCH values for all colors and their shades.

Example:

```json
{
    "red": {
        "50": "oklch(97% 0.12 23)",
        "100": "oklch(93% 0.20 23)",
        ...
    },
    "blue": {
        "50": "oklch(98% 0.08 264)",
        "100": "oklch(94% 0.17 264)",
        ...
    }
}
```

## Resources

-   **Tailwind CSS Documentation**: [https://tailwindcss.com/docs/background-color](https://tailwindcss.com/docs/background-color)
-   **Python OKLCH Library**: [https://github.com/arkonger/python-oklch](https://github.com/arkonger/python-oklch)

## Notes

-   This script assumes that the structure of the Tailwind CSS documentation remains consistent.
-   The conversion function ensures the output adheres to the OKLCH format required by Tailwind CSS V4.

## License

This project is open-source and available under the MIT License.
