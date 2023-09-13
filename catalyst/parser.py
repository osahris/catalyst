import os

#from staticsite.utils.front_matter import read_whole as read_front_matter_markdown

import frontmatter

def read_catalyst_directory(dirname):
    print("Reading catalyst markdown directory: " + dirname)

    # Get all the files in the directory and all subdirectories
    files = []
    for (dirpath, dirnames, filenames) in os.walk(dirname):
        for filename in filenames:
            files.append(os.path.join(dirpath, filename))

    # Filter out all non-markdown files
    var_files = []
    class_files = []
    valueset_files = []
    codesystem_files = []
    for filename in files:
        if filename.endswith(".var.md"):
            var_files.append(filename)
        elif filename.endswith(".class.md"):
            class_files.append(filename)
        elif filename.endswith(".valueset.md"):
            valueset_files.append(filename)
        elif filename.endswith(".codesystem.md"):
            codesystem_files.append(filename)

    vars = {}
    classes = {}
    valuesets = {}
    codesystems = {}

    # TODO cleanup

    # Generate a dictionary of markdown files, keyed by filename
    for filename in var_files:
        # we only want the filename without the path
        key = os.path.basename(filename)
        # remove the .var.md extension
        key = key[:-7]
        vars[key] = read_catalyst_markdown_file(filename)
    for filename in class_files:
        # we only want the filename without the path
        key = os.path.basename(filename)
        # remove the .class.md extension
        key = key[:-9]
        classes[key] = read_catalyst_markdown_file(filename)
    for filename in valueset_files:
        # we only want the filename without the path
        key = os.path.basename(filename)
        # remove the .valueset.md extension
        key = key[:-12]
        valuesets[key] = read_catalyst_markdown_file(filename)
    for filename in codesystem_files:
        # we only want the filename without the path
        key = os.path.basename(filename)
        # remove the .codesystem.md extension
        key = key[:-14]
        codesystems[key] = read_catalyst_markdown_file(filename)

    return {
        "vars": vars,
        "classes": classes,
        "valuesets": valuesets,
        "codesystems": codesystems
    }

def read_catalyst_markdown_file(filename):
    print("Reading catalyst markdown file: " + filename)
    with open(filename, 'rt') as file:
        fmt = frontmatter.load(file)
    r = fmt.metadata
    if len(fmt.content) > 0:
        r["UnstructuredContent"] = fmt.content
    return r
