from zipfile import ZipFile

local_dependencies = [
    "requirements.txt",
    "main.py"
]
aliased_dependencies = {
    "../../src/features/build_features.py": "features/build_features.py",
    "../../src/features/url.py": "features/url.py",
    "../../src/features/url_utils.py": "features/url_utils.py"
}


if __name__ == "__main__":
    print("Creating ZIP for feature extraction endpoint")

    with ZipFile("getFeaturesFromUrl.zip", "w") as dist:
        for file in local_dependencies:
            dist.write(file)
            print("Added [%s] to zip" % file)

        for real_file, arc_file in aliased_dependencies.items():
            dist.write(real_file, arcname=arc_file)
            print("Added [%s] to zip" % real_file)

    print("Created ZIP for feature extraction endpoint successfully")
