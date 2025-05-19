from pptx2md import convert, ConversionConfig
from pathlib import Path
from tempfile import TemporaryDirectory
import os

def pptx_to_md(pptx_path: Path, image_dir: str | None = None) -> list[str]:
    with TemporaryDirectory() as tmp_dir:
        convert(
            ConversionConfig(
                pptx_path=pptx_path,
                output_path=Path(os.path.join(tmp_dir, "output.md")),
                image_dir=Path(image_dir),
                disable_image=image_dir is None,
                disable_notes=True,
                disable_color=True,
                enable_slides=True,
                min_img_size=200,
            )
        )

        with open(os.path.join(tmp_dir, "output.md")) as f:
            md_content = f.read()

        print(md_content)

        return md_content.split("\n---\n")
    return None

def main() -> None:
    pptx_to_md("/Users/thermens/Desktop/powerpoint_foo.pptx", "/Users/thermens/Documents/pptx2md/imgs")


if __name__ == "__main__":
    main()
