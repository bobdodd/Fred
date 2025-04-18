#!/usr/bin/env python
import os
import click
from pathlib import Path
from pdf2image import convert_from_path


@click.command()
@click.option('--pdf-path', required=True, type=click.Path(exists=True), help='Path to the PDF file')
@click.option('--output-dir', required=True, type=click.Path(), help='Directory to save the PNG images')
@click.option('--dpi', default=300, help='DPI resolution for the images')
@click.option('--prefix', default='page_', help='Prefix for the output filenames')
@click.option('--first-page', default=1, help='First page to convert (1-based)')
@click.option('--last-page', default=None, type=int, help='Last page to convert (inclusive)')
def convert_pdf_to_png(pdf_path, output_dir, dpi, prefix, first_page, last_page):
    """Convert a PDF document to a set of PNG images, one for each page."""
    
    # Create output directory if it doesn't exist
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Convert PDF to images
    images = convert_from_path(
        pdf_path, 
        dpi=dpi, 
        first_page=first_page,
        last_page=last_page
    )
    
    # Save images
    for i, image in enumerate(images):
        page_num = i + first_page
        output_file = output_path / f"{prefix}{page_num:03d}.png"
        image.save(output_file, "PNG")
        click.echo(f"Saved {output_file}")
    
    click.echo(f"Converted {len(images)} pages from {pdf_path} to PNG images")


if __name__ == "__main__":
    convert_pdf_to_png()